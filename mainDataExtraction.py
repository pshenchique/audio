from audioGeneration import playSound
from colorDataCalculation import calculate_colorfulness, calculate_warmness_coldness
from intensityCalculation import extract_features, normalize_dict_values


def allImages():
    intensity_values = {}
    warmness_values = {}
    colorfulness_values = {}

    for i in range (1, 11):
        image_path = f'data/{i}.jpg'
        intensity_values[i] = int(extract_features(image_path))

        warmness_values[i] = calculate_warmness_coldness(image_path)
        colorfulness_values[i] = calculate_colorfulness(image_path)

    warmness_values = normalize_dict_values(warmness_values, 0, 100)
    colorfulness_values = normalize_dict_values(colorfulness_values, 100, 0)

    print(f'intensity: {dict(sorted(intensity_values.items(), key=lambda item: item[1], reverse=True))}')
    print(f'warmness: {dict(sorted(warmness_values.items(), key=lambda item: item[1], reverse=True))}')
    print(f'colorfulness: {dict(sorted(colorfulness_values.items(), key=lambda item: item[1], reverse=True))}')

    i = 4

    playSound(intensity_values[i], warmness_values[i], colorfulness_values[i])



# def oneImage(i):
#     image_path = f'data/{i}.jpg'
#     intensity_score = extract_features(image_path)
#     # print(f"Intensity Score of image #{i}: {intensity_score}")

#     warmness_values = {}
#     colorfulness_values = {}

#     warmness_values[i] = calculate_warmness_coldness(image_path)
#     colorfulness_values[i] = calculate_colorfulness(image_path)

#     warmness_values = normalize_dict_values(warmness_values, 0, 100)
#     colorfulness_values = normalize_dict_values(colorfulness_values, 100, 0)

#     playSound(intensity_score, warmness_values[i], colorfulness_values[i])



allImages()
# oneImage(1)