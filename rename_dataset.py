import os
import shutil

# Use current directory as base path
base_path = "."

# Final destination folder
destination = os.path.join(base_path, "data")

# Create the final 'data' folder if it doesn't exist
os.makedirs(destination, exist_ok=True)

# Go through all folders in the current directory
for folder_name in os.listdir(base_path):
    folder_path = os.path.join(base_path, folder_name)
    
    # Select only folders that start with 'data ' (like 'data 3', 'data 4', etc.), but skip the final 'data' folder
    if os.path.isdir(folder_path) and folder_name.startswith("data ") and folder_name.strip() != "data":
        print(f"📁 Processing folder: {folder_name}")
        
        # Go through each subfolder (a, b, 0, 1, ...)
        for subfolder_name in os.listdir(folder_path):
            subfolder_path = os.path.join(folder_path, subfolder_name)

            if os.path.isdir(subfolder_path):
                # Normalize the subfolder name (e.g., A -> a)
                normalized_name = subfolder_name.lower()

                # Create the target subfolder in 'data'
                target_folder = os.path.join(destination, normalized_name)
                os.makedirs(target_folder, exist_ok=True)

                # Loop over each image
                for file_name in os.listdir(subfolder_path):
                    src_file = os.path.join(subfolder_path, file_name)
                    dst_file = os.path.join(target_folder, file_name)

                    # If the destination file already exists, rename it to avoid overwrite
                    if os.path.exists(dst_file):
                        base, ext = os.path.splitext(file_name)
                        i = 1
                        while True:
                            new_name = f"{base}_{i}{ext}"
                            dst_file = os.path.join(target_folder, new_name)
                            if not os.path.exists(dst_file):
                                break
                            i += 1

                    # Copy file to destination
                    shutil.copy2(src_file, dst_file)

print("✅ All data merged into 'data/' folder with no filename conflicts.")
