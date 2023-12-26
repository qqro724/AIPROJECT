from models.ImageGener import StyleGAN

model=StyleGAN()
model2=tacotron()

for epoch in epochs:
    for idx,data in enumerate(dataloader):