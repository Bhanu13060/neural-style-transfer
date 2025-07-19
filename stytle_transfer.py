# Load images
content = image_loader('data/content.jpg')
style = image_loader('data/style.jpg')

# Create a model (e.g. VGG19)
# Extract features, define loss, optimize

output = run_style_transfer(content, style)
save_image(output, 'data/output.jpg')
