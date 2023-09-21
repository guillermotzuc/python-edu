import os

#stage = os.environ['STAGE'].upper()
stage = os.getenv('STAGE', 'dev').upper()

output = f"We're running in {stage}"

if stage.startswith('PROD'):
    output = "DANGER!!! - " + output

print(output)