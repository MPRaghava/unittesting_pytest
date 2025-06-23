from typing import List

def simple_chunking(text:str,max_words : int =50) -> list[str]:
    chunks =[]
    words = text.split()
    for i in range(0,len(words),max_words):
        chunk = " ".join(words[i:i + max_words])
        chunks.append(chunk)
    return chunks


# text = """ Gold mining is the process of extracting gold from the earth, either from rocks or river sediments.
# It includes methods like placer mining, hard rock mining, open-pit mining, and underground mining.
# Placer mining uses water and gravity to separate gold from loose materials.
# Hard rock mining involves drilling and blasting to extract gold ore from deep underground.
# Open-pit mining creates large surface excavations, while underground mining uses shafts and tunnels.
# The extracted ore is crushed, concentrated, and treated with chemicals like cyanide to isolate gold.
# Smelting then purifies the gold into bars for commercial use.
# Leading gold producers include China, Australia, Russia, the USA, and Canada.
# Gold is widely used in jewelry, electronics, medicine, and as a financial asset.
# Mining operations can lead to deforestation, habitat destruction, and water pollution.
# Toxic chemicals like mercury and cyanide pose environmental and health risks.
# Illegal mining can exploit workers and harm local communities.
# Sustainable mining practices are being adopted to reduce environmental impact.
# Gold is often seen as a hedge against inflation and economic instability.
# All the gold ever mined would fit into a cube approximately 22 meters on each side.

# Let me know if you'd like this in Telugu or converted into a slide deck."""
# result = simple_chunking(text)
# # print(result)
# for c in enumerate(result):
#     print(c)
#     print("\n"*2)
