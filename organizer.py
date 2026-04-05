            try:
                if dry_run:
                    print(f"[DRY RUN] {file} -> {category}/")
                else:
                    if not os.path.exists(target_dir):
                        os.makedirs(target_dir)

                    if os.path.exists(target_path):
                        print(f"Skipping {file}, already exists")
                        continue

                    shutil.move(full_path, target_path)
                    print(f"Moved {file} -> {category}/")

            except Exception as e:
                print(f"Error processing {file}: {e}")