from diffusers import StableDiffusionAdapterPipeline

pipe = StableDiffusionAdapterPipeline.from_pretrained('CompVis/stable-diffusion-v1-4')

prompt = "in the desert, a corvette parked in front of an old-school diner at sundown"

image = pipe(prompt).images[0]
image.save("picture.jpg")