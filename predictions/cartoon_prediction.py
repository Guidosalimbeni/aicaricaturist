import replicate
import requests

# Initialize client with token
client = replicate.Client(api_token="33fb8a9e8bcaa47fe78ec57155cdf0dda9bfe883")


input = {
    "prompt": "cartoon caricature in CRTFLX01 style of a woman with short dark brown hair styled into a voluminous updo, pink background, wearing a high-necked, long-sleeved golden-yellow top, slender neck, bright blue eyes looking to the side, eyebrows arched in a playful expression, small stud earrings, mouth open in an “o” shape revealing slightly parted lips, cheeks lightly blushed, rendered in a caricature style with exaggerated facial features, cartoon, digital illustration.",
    "output_format": "png",
    "output_quality": 85,
    "prompt_strength": 0.85
}

output = client.run(
    "guidosalimbeni/cartoon-flux:324b8389b851bd117554dcb4df772a4f4b54d825a3e9cad7fb5d83cfa35a6f98",
    input=input
)

for index, item in enumerate(output):
    response = requests.get(item)
    with open(f"output_{index}.png", "wb") as file:
        file.write(response.content)
    print(f"output_{index}.png written to disk")
