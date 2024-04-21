import os
import google.generativeai as genai
from dotenv import load_dotenv
import os
import json

genAI = genai.configure(api_key=os.getenv("api_key"))

def configure():
  load_dotenv()

def run():
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content("""Can you create a customized weekly workout plan for me? Please structure the response in a JSON format. The plan should include an array for 'body_composition' details, an array of 'Tips' for effective workouts, and a 'WeekPlan' detailing three different workouts. Each workout should have a specific name reflecting its focus (e.g., Full Body, Upper Body Strength, Lower Body Strength) and include two exercises. Specify the name, reps, and sets for each exercise. Use this structure for guidance:
json

Copy code
{ "body_composition": [ { "type": "ExampleType1", "value": "ExampleValue1" }, { "type": "ExampleType2", "value": "ExampleValue2" } ], "Tips": [ "Tip1: Example Tip Content 1", "Tip2: Example Tip Content 2" ], "WeekPlan": { "workout1": { "name": "Full Body Workout", "exercise1": { "name": "Exercise Name 1", "reps": "10", "sets": "3" }, "exercise2": { "name": "Exercise Name 2", "reps": "12", "sets": "4" } }, "workout2": { "name": "Upper Body Strength", "exercise1": { "name": "Exercise Name 3", "reps": "15", "sets": "3" }, "exercise2": { "name": "Exercise Name 4", "reps": "10", "sets": "2" } }, "workout3": { "name": "Lower Body Strength", "exercise1": { "name": "Exercise Name 5", "reps": "20", "sets": "5" }, "exercise2": { "name": "Exercise Name 6", "reps": "8", "sets": "3" } } } } 
Please replace the example types, values, tips, and exercise details with those suited to my goals of [insert your specific goals here, e.g., gaining muscle, losing weight, increasing endurance]. with my body comp data as Date Weight (lb) Fat mass (lb) Bone Mass (lb) Muscle Mass (lb) Water Weight (lb) 4/20/24 20:35 228.3 59.1 8.4 160.7 115.1 4/20/24 20:22 227.8 59 8.4 160.4 114.7""")

    if response.parts:
      response_text = response.parts[0].text.strip()
      if response_text:
          try:
              json_response = json.loads(response_text)
              with open('workout_plan.json', 'w') as file:
                  json.dump(json_response, file, indent=4)
              print("JSON file saved successfully!")
          except json.JSONDecodeError as e:
              print(f"Error parsing JSON: {e}")
      else:
          print("Response was empty.")
    else:
      print("Response was blocked or no content was returned.")
run() 
