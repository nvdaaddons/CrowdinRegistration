#!/usr/bin/env python3
"""Clone all NVDA add-on repositories into a tempAddon folder."""

import json
import os
import subprocess
import sys
from pathlib import Path

import requests


def get_addon_repositories():
	"""Fetch add-on repository URLs from the NVDA add-on store."""
	print("Fetching add-on list from NVDA add-on store...")
	url = "https://addonStore.nvaccess.org/en/all/latest.json"
	response = requests.get(url, timeout=30)
	response.raise_for_status()
	
	addons = response.json()
	
	# Extract repository URLs (base URL without /releases or specific paths)
	addon_repos = {}
	for addon in addons:
		addon_id = addon.get("addonId")
		source_url = addon.get("sourceURL")
		
		if addon_id and source_url:
			# Extract base repository URL (first 5 parts of the URL)
			parts = source_url.split("/")
			if len(parts) >= 5:
				base_url = "/".join(parts[:5])
				addon_repos[addon_id] = base_url
	
	return addon_repos


def clone_repositories(addon_repos, target_dir):
	"""Clone each add-on repository into the target directory."""
	target_path = Path(target_dir)
	target_path.mkdir(exist_ok=True)
	
	print(f"\nCloning {len(addon_repos)} add-on repositories into {target_dir}...\n")
	
	success_count = 0
	failed_addons = []
	
	for addon_id, repo_url in addon_repos.items():
		addon_path = target_path / addon_id
		
		# Skip if already cloned
		if addon_path.exists():
			print(f"⏭️  {addon_id}: Already exists, skipping")
			success_count += 1
			continue
		
		print(f"📥 Cloning {addon_id} from {repo_url}...")
		
		try:
			# Clone the repository
			result = subprocess.run(
				["git", "clone", repo_url, str(addon_path)],
				capture_output=True,
				text=True,
				timeout=120
			)
			
			if result.returncode == 0:
				print(f"✅ {addon_id}: Successfully cloned")
				success_count += 1
			else:
				print(f"❌ {addon_id}: Failed to clone")
				print(f"   Error: {result.stderr.strip()}")
				failed_addons.append(addon_id)
		
		except subprocess.TimeoutExpired:
			print(f"❌ {addon_id}: Clone timeout")
			failed_addons.append(addon_id)
		except Exception as e:
			print(f"❌ {addon_id}: Error - {e}")
			failed_addons.append(addon_id)
	
	# Summary
	print("\n" + "=" * 60)
	print(f"Summary: {success_count}/{len(addon_repos)} repositories processed")
	if failed_addons:
		print(f"\nFailed add-ons ({len(failed_addons)}):")
		for addon_id in failed_addons:
			print(f"  - {addon_id}")
	print("=" * 60)


def main():
	"""Main entry point."""
	# Get the repository root
	script_dir = Path(__file__).parent
	repo_root = script_dir.parent
	temp_addon_dir = repo_root / "tempAddon"
	
	try:
		# Fetch add-on repository URLs
		addon_repos = get_addon_repositories()
		
		# Save the addon list for reference
		addon_list_file = repo_root / "addons.json"
		with open(addon_list_file, "w", encoding="utf-8") as f:
			json.dump(addon_repos, f, indent=2)
		print(f"Saved add-on list to {addon_list_file}")
		
		# Clone repositories
		clone_repositories(addon_repos, temp_addon_dir)
		
	except requests.RequestException as e:
		print(f"Error fetching add-on list: {e}", file=sys.stderr)
		sys.exit(1)
	except KeyboardInterrupt:
		print("\n\nCloning interrupted by user")
		sys.exit(1)
	except Exception as e:
		print(f"Unexpected error: {e}", file=sys.stderr)
		sys.exit(1)


if __name__ == "__main__":
	main()
