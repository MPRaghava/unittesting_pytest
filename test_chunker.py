from chunker import simple_chunking

text = """ Gold mining is the process of extracting gold from the earth, either from rocks or river sediments.
It includes methods like placer mining, hard rock mining, open-pit mining, and underground mining.
Placer mining uses water and gravity to separate gold from loose materials.
Hard rock mining involves drilling and blasting to extract gold ore from deep underground.
Open-pit mining creates large surface excavations, while underground mining uses shafts and tunnels.
The extracted ore is crushed, concentrated, and treated with chemicals like cyanide to isolate gold.
Smelting then purifies the gold into bars for commercial use.
Leading gold producers include China, Australia, Russia, the USA, and Canada.
Gold is widely used in jewelry, electronics, medicine, and as a financial asset.
Mining operations can lead to deforestation, habitat destruction, and water pollution.
Toxic chemicals like mercury and cyanide pose environmental and health risks.
Illegal mining can exploit workers and harm local communities.
Sustainable mining practices are being adopted to reduce environmental impact.
Gold is often seen as a hedge against inflation and economic instability.
All the gold ever mined would fit into a cube approximately 22 meters on each side.

Let me know if you'd like this in Telugu or converted into"""
 
def test_chunking_basic():
    max_words = 50
    word_count = len(text.split())
    # print(word_count)
    chunks = simple_chunking(text.strip(),max_words)
    # assert len(chunks) == 4
    # assert len(chunks[0].strip()) == 50 
    assert len(chunks) == (word_count + max_words - 1) // max_words  # ceiling division
    assert len(chunks[0].split()) == 50 


def test_chunking_short_text():
    text = "only ten words here now for this short test case"
    chunks = simple_chunking(text.strip(), max_words=10)
    assert len(chunks) == 1
    assert chunks[0] == text