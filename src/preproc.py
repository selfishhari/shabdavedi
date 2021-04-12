def unzip_data(fname, dest_folder):

    with zipfile.ZipFile(fname, 'r') as zip_ref:

        zip_ref.extractall(dest_folder)

def download_and_extract(name="openslr_kannada", out_folder = ""):
    if name=="openslr_kannada":

        url_list = ["https://www.openslr.org/resources/79/kn_in_male.zip", "https://www.openslr.org/resources/79/kn_in_female.zip"]

        out_paths = [os.path.join(out_folder, "kn_in_male.zip"), os.path.join(out_folder, "kn_in_female.zip")]

        unzip_paths = [os.path.join(out_folder, "kn_in_male"), os.path.join(out_folder, "kn_in_female")]

        url_paths = zip(url_list, out_paths, unzip_paths)

    for u, p, uz in url_paths:
        
        print("Downloading ", u, "to", p)
        urllib.request.urlretrieve(u, p)
        print("Unzipping to:", uz)
        unzip_data(p, uz)

#download_and_extract(name="openslr_kannada", out_folder = raw_dir)