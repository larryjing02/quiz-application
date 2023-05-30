from bing_image_downloader import downloader

# List of plant families
plant_families = ['Asteraceae', 'Adoxaceae', 'Berberidaceae', 'Plantaginaceae', 'Apiaceae', 'Iridaceae', 'Polemoniaceae', 'Rosaceae', 'Onagraceae', 'Aceraceae', 'Hamamelidaceae', 'Oleaceae', 'Brassicaceae', 'Lauraceae', 'Araceae', 'Fagaceae', 'Salicaceae', 'Violaceae', 'Saxifragaceae', 'Fabaceae', 'Caryophyllaceae', 'Cactaceae', 'Montiaceae', 'Ericaceae', 'Cornaceae', "Dubs", 'Solanaceae', 'Hydrophyllaceae', 'Boraginaceae', 'Juncaceae', 'Cyperaceae', 'Poaceae', 'Typhaceae', 'Orchidaceae', 'Liliaceae', 'Magnoliaceae', 'Betulaceae', 'Ranunculaceae', 'Lamiaceae', 'Caprifoliaceae']

# Function to download images for each plant family
def download_images_for_families(families, num_images=4, output_dir="img"):
    for family in families:
        # Download images
        downloader.download(family, limit=num_images, output_dir=output_dir, 
                            adult_filter_off=True, force_replace=False, timeout=60)

# Call the function
download_images_for_families(plant_families)
