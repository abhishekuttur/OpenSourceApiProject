import json

def parse_text_to_json(text):
    # Split the text into Step#1 and Step#2 outputs
    step1_output, step2_output = text.split("Step#2 Output:")

    # Function to parse each step's output into JSON format
    def parse_step_output(step_output):
        import pdb;pdb.set_trace()
        # Remove leading and trailing whitespaces and newlines
        step_output = step_output.strip()

        # Extract the list of attacks from the step output
        attacks_list = step_output.split("[")[1].split("]")[0]

        # Split the attacks list into individual attack descriptions
        attacks = attacks_list.split("{")[1:]

        # Initialize a list to store parsed attacks
        parsed_attacks = []

        # Parse each attack description
        for attack in attacks:
            # Extract attack properties
            attack_properties = attack.split(",\n")

            # Initialize a dictionary to store attack information
            attack_info = {}

            # Parse attack properties and add them to the attack dictionary
            for prop in attack_properties:
                if prop.strip() == "" or prop.strip() == ",":
                    continue
                key, value = prop.strip().split(": ")
                attack_info[key.strip('"')] = value.strip('"')

            # Append the parsed attack to the list of parsed attacks
            parsed_attacks.append(attack_info)

        return parsed_attacks

    # Parse Step#1 output into JSON format
    step1_json = parse_step_output(step1_output)

    # Parse Step#2 output into JSON format
    step2_json = parse_step_output(step2_output)

    return step1_json, step2_json

# Example usage:
your_text = '\n\n\nStep#1 Output:\n[\n  {\n    "Attack_id": 1,\n    "Level": 1,\n    "Title": "Denial of Service (DoS) Attack",\n    "Description": "An attacker floods the CAN bus with a large number of messages, causing the system to crash or become unresponsive.",\n    "Type of Attack": "Physical"\n  },\n  {\n    "Attack_id": 2,\n    "Level": 1,\n    "Title": "Man-in-the-Middle (MitM) Attack",\n    "Description": "An attacker intercepts and modifies messages on the CAN bus, allowing them to inject malicious commands or alter data.",\n    "Type of Attack": "Network"\n  },\n  {\n    "Attack_id": 3,\n    "Level": 1,\n    "Title": "Replay Attack",\n    "Description": "An attacker records legitimate messages on the CAN bus and replays them at a later time to gain unauthorized access or cause system malfunctions.",\n    "Type of Attack": "Network"\n  },\n  {\n    "Attack_id": 4,\n    "Level": 1,\n    "Title": "Firmware/Software Attack",\n    "Description": "An attacker exploits vulnerabilities in the ECU\'s firmware or software to gain access to the CAN bus and manipulate data or commands.",\n    "Type of Attack": "Software"\n  },\n  {\n    "Attack_id": 5,\n    "Level": 1,\n    "Title": "Physical Attack",\n    "Description": "An attacker physically accesses the CAN bus or ECU to tamper with hardware components or install malicious devices.",\n    "Type of Attack": "Physical"\n  }\n]\n\nStep#2 Output:\n[\n  {\n    "Attack_id": 1,\n    "Level": 2,\n    "Title": "Flooding Attack",\n    "Description": "An attacker sends a large number of messages to the CAN bus, overwhelming the system and causing a DoS.",\n    "Type of Attack": "Physical"\n  },\n  {\n    "Attack_id": 1,\n    "Level": 2,\n    "Title": "Jamming Attack",\n    "Description": "An attacker continuously transmits noise on the CAN bus, disrupting communication and causing a DoS.",\n    "Type of Attack": "Physical"\n  },\n  {\n    "Attack_id": 1,\n    "Level": 2,\n    "Title": "Bus Off Attack",\n    "Description": "An attacker sends a series of error frames to the CAN bus, causing the system to go into a Bus Off state and become unresponsive.",\n    "Type of Attack": "Physical"\n  },\n  {\n    "Attack_id": 2,\n    "Level": 2,\n    "Title": "Message Modification",\n    "Description": "An attacker intercepts and modifies messages on the CAN bus, allowing them to inject malicious commands or alter data.",\n    "Type of Attack": "Network"\n  },\n  {\n    "Attack_id": 2,\n    "Level": 2,\n    "Title": "Message Injection",\n    "Description": "An attacker injects new messages onto the CAN bus, bypassing authentication and authorization mechanisms.",\n    "Type of Attack": "Network"\n  },\n  {\n    "Attack_id": 2,\n    "Level": 2,\n    "Title": "Message Replay",\n    "Description": "An attacker replays previously captured messages on the CAN bus, bypassing authentication and authorization mechanisms.",\n    "Type of Attack": "Network"\n  },\n  {\n    "Attack_id": 3,\n    "Level": 2,\n    "Title": "Message Recording",\n    "Description": "An attacker records legitimate messages on the CAN bus and replays them at a later time to gain unauthorized access or cause system malfunctions.",\n    "Type of Attack": "Network"\n  },\n  {\n    "Attack_id": 3,\n    "Level": 2,\n    "Title": "Message Manipulation",\n    "Description": "An attacker modifies the contents of recorded messages before replaying them, allowing them to inject malicious commands or alter data.",\n    "Type of Attack": "Network"\n  },\n  {\n    "Attack_id": 3,\n    "Level": 2,\n    "Title": "Message Deletion",\n    "Description": "An attacker deletes recorded messages on the CAN bus, causing system malfunctions or disrupting communication.",\n    "Type of Attack": "Network"\n  },\n  {\n    "Attack_id": 4,\n    "Level": 2,\n    "Title": "Buffer Overflow",\n    "Description": "An attacker exploits a buffer overflow vulnerability in the ECU\'s firmware or software to gain access to the CAN bus and manipulate data or commands.",\n    "Type of Attack": "Software"\n  },\n  {\n    "Attack_id": 4,\n    "Level": 2,\n    "Title": "Code Injection",\n    "Description": "An attacker injects malicious code into the ECU\'s firmware or software, allowing them to gain access to the CAN bus and manipulate data or commands.",\n    "Type of Attack": "Software"\n  },\n  {\n    "Attack_id": 4,\n    "Level": 2,\n    "Title": "Firmware Update Attack",\n    "Description": "An attacker exploits vulnerabilities in the ECU\'s firmware update process to install malicious firmware, gaining access to the CAN bus and manipulating data or commands.",\n    "Type of Attack": "Software"\n  },\n  {\n    "Attack_id": 5,\n    "Level": 2,\n    "Title": "ECU Tampering",\n    "Description": "An attacker physically accesses the ECU and modifies hardware components, allowing them to manipulate data or commands on the CAN bus.",\n    "Type of Attack": "Physical"\n  },\n  {\n    "Attack_id": 5,\n    "Level": 2,\n    "Title": "Device Installation",\n    "Description": "An attacker installs a malicious device on the CAN bus, allowing them to intercept and modify messages or inject commands.",\n    "Type of Attack": "Physical"\n  },\n  {\n    "Attack_id": 5,\n    "Level": 2,\n    "Title": "ECU Replacement",\n    "Description": "An attacker replaces a legitimate ECU with a malicious one, gaining access to the CAN bus and manipulating data or commands.",\n    "Type of Attack": "Physical"\n  }\n]'
step1_json, step2_json = parse_text_to_json(your_text)

# Convert the parsed JSON to a string
step1_json_str = json.dumps(step1_json, indent=2)
step2_json_str = json.dumps(step2_json, indent=2)

print("Step#1 Output:")
print(step1_json_str)
print("\nStep#2 Output:")
print(step2_json_str)
