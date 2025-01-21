
!pip install -q google-generativeai
import google.generativeai as palm
palm.configure(api_key="AIzaSyCvj5zQxqZLDJaPkWxYhBzYJ7a1I8v9whQ")
models = [
    m for m in palm.list_models() if "generateText" in m.supported_generation_methods
]

for m in models:
    print(f"Model Name: {m.name}")
Model Name: models/text-bison-001
model = models[0].name
model
'models/text-bison-001'
prompt = """
Summarize this paragraph and detail some relevant context.

Text: "I am by birth a Genevese, and my family is one of the most distinguished of that republic. My ancestors had been for many years counsellors and syndics, and my father had filled several public situations with honour and reputation. He was respected by all who knew him for his integrity and indefatigable attention to public business. He passed his younger days perpetually occupied by the affairs of his country; a variety of circumstances had prevented his marrying early, nor was it until the decline of life that he became a husband and the father of a family."

Summary: In this text, the narrator is describing his background and upbringing. He tells us that he is a native of Geneva, Switzerland, and that his family is one of the most distinguished in the republic. He then goes on to describe his father, who was a respected public servant.

Text: "The thing the Time Traveller held in his hand was a glittering metallic framework, scarcely larger than a small clock, and very delicately made. There was ivory in it, and some transparent crystalline substance. And now I must be explicit, for this that follows—unless his explanation is to be accepted—is an absolutely unaccountable thing. He took one of the small octagonal tables that were scattered about the room, and set it in front of the fire, with two legs on the hearthrug."

"""
completion = palm.generate_text(
    model=model,
    prompt=prompt,
    temperature=0.3,
    # The maximum length of the response
    max_output_tokens=800,
)

print(completion.result)
Summary: The Time Traveller holds a glittering metallic framework in his hand. It is very small and delicate, with ivory and some transparent crystalline substance. He sets it on a table in front of the fire.
 
 
 
 
 
 
 
Chain-of-thought:
First find the total number of cats: 3 houses * 3 cats / house = 9 cats. Then multiply the number of cats by the number of mittens per cat to find the total number of mittens: 9 cats * 4 mittens / cat = 36 mittens. Then multiply the number of mittens by the length of yarn per mitten to find the total length of yarn used for mittens: 36 mittens * 7m / mitten = 252m. Then multiply the number of cats by the number of hats per cat to find the total number of hats: 9 cats * 1 hat / cat = 9 hats. Then multiply the number of hats by the length of yarn per hat to find the total length of yarn used for hats: 9 hats * 4m / hat = 36m. Then add the length of yarn used for mittens and hats to find the total length of yarn used: 252m + 36m = 288m.

The answer should be 288
print(equation)
 3 houses * 3 cats/house 
 
 
 
 
 
 
 
calc_prompt = f"""
Please solve the following problem.

{prompt}

----------------

Important: Use the calculator for each step.
Don't do the arithmetic in your head. 

To use the calculator wrap an equation in <calc> tags like this: 

<calc> 3 cats * 2 hats/cat </calc> = 6

----------------

"""

equation = None
while equation is None:
    completion = palm.generate_text(
        model=model,
        prompt=calc_prompt,
        stop_sequences=["</calc>"],
        # The maximum length of the response
        max_output_tokens=800,
    )

    try:
        response, equation = completion.result.split("<calc>", maxsplit=1)
    except Exception:
        continue
print(response)
**Step 1:** Count the number of cats in all three houses:


 
