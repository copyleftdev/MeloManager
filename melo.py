import json
import collections


class MeloManager(object):

    def load_behavior(self, content):
        device = content['AppData']['Device']
        screen_res = content['AppData']['ScreenSize']
        touch_events = content['EventModels']['TouchEvents']
        text_events = content['EventModels']['TextInputEvents']
        dropdown_events = content['EventModels']['DropdownEvents']
        toggle_events = dropdown_events = content['EventModels']['ToggleEvents']
        steps = []
        for touch in touch_events:
            steps.append(touch)
        for text in text_events:
            steps.append(text)
        for drop in dropdown_events:
            steps.append(drop)
        for toggle in toggle_events:
            steps.append(toggle)

        sorted_steps = sorted(steps, reverse=True, key=lambda k: k['Timestamp'])

        master_record = {"device": device, "screen_resolution": screen_res,
                         "steps": sorted_steps}
        return master_record


with open("data/sample.json") as out:
    content = json.load(out)


m = MeloManager()
result = m.load_behavior(content)
j = json.dumps(result)
print(j)
