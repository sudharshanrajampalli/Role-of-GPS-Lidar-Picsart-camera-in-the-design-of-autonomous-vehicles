import replicate
output = replicate.run(
    "sczhou/codeformer:7de2ea26c616d5bf2245ad0d5e24f0ff9a6204578a5c876db53142edd9d2cd56",
    input={
        "image": "https://replicate.delivery/pbxt/IngEkQmZiZ3whtbkNAiOIdCsYAWVMkmoIBJnw7t2TPgvJn5S/photo.jpg",
        "upscale": 1,
        "face_upsample": True,
        "background_enhance": True,
        "codeformer_fidelity": 0.7
    }
)
print(output)