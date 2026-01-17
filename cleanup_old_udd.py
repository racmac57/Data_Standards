import os
import shutil

# Navigate to the problematic directory
base = r"C:\Users\carucci_r\OneDrive - City of Hackensack\09_Reference\Standards"
target = os.path.join(base, "unified_data_dictionary")

print(f"Attempting to remove: {target}")

if os.path.exists(target):
    try:
        # Try shutil first
        shutil.rmtree(target, ignore_errors=True)
        print("✓ Successfully removed using shutil")
    except Exception as e:
        print(f"shutil failed: {e}")
        # Try os.system with subst (map to drive letter)
        try:
            import subprocess
            # Map to Z: drive to shorten path
            subprocess.run("subst Z: .", shell=True, cwd=base, check=False)
            subprocess.run("rmdir /s /q Z:\\unified_data_dictionary", shell=True, check=False)
            subprocess.run("subst Z: /d", shell=True, check=False)
            print("✓ Successfully removed using subst workaround")
        except Exception as e2:
            print(f"subst workaround also failed: {e2}")
else:
    print("Directory does not exist - already clean!")

# Verify
if not os.path.exists(target):
    print("\n✓✓✓ MIGRATION COMPLETE - Old directory removed!")
else:
    print("\n⚠ Directory still exists - manual removal may be needed")
