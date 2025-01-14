from llama_index.llms.ollama import Ollama

def dialog_between_models(num_turns):
    # Create two instances of the model with personality context
    llm1 = Ollama(model='llama3.1:8b')  # Specify the model for Anna
    llm2 = Ollama(model='llama3.1:8b')  # Specify the model for Bob

    # Define personalities
    persona1 = ""  # Personality description for Anna
    persona2 = ""  # Personality description for Bob

    # Initial message
    dialog_full = []
    dialog_anna = []
    dialog_bob = []

    for i in range(num_turns):
        if i == 0:
            # Model 1 thinks
            thought1 = llm1.complete(f"{persona1} Think about your situation.")
            dialog_full.append(f"**Anna thinks:** {thought1}")
            dialog_anna.append(f"**Anna thinks:** {thought1}")
            
            # Model 1 speaks
            response1 = llm1.complete(f"{persona1} Say something.")
            dialog_full.append(f"**Anna says:** {response1}")
            dialog_anna.append(f"**Anna says:** {response1}")
            dialog_bob.append(f"**Anna says:** {response1}")
        else:
            # Model 1 thinks after hearing Bob
            thought1 = llm1.complete(f"{persona1} You hear someone say: '{message}'. Think about your situation. Here is what was said earlier: {' '.join(dialog_full)}")
            dialog_full.append(f"**Anna thinks:** {thought1}")
            dialog_anna.append(f"**Anna thinks:** {thought1}")
            
            # Model 1 speaks based on its thoughts and what it heard
            response1 = llm1.complete(f"{persona1} Based on your thoughts: '{thought1}', respond to: '{message}'. Here is what was said earlier: {' '.join(dialog_full)}")
            dialog_full.append(f"**Anna says:** {response1}")
            dialog_anna.append(f"**Anna says:** {response1}")
            dialog_bob.append(f"**Anna says:** {response1}")
        
        # Model 2 thinks after hearing Anna
        thought2 = llm2.complete(f"{persona2} You hear someone say: '{response1}'. Think about your situation. Here is what was said earlier: {' '.join(dialog_full)}")
        dialog_full.append(f"**Bob thinks:** {thought2}")
        dialog_bob.append(f"**Bob thinks:** {thought2}")
        
        # Model 2 speaks based on its thoughts and what it heard
        response2 = llm2.complete(f"{persona2} Based on your thoughts: '{thought2}', respond to: '{response1}'. Here is what was said earlier: {' '.join(dialog_full)}")
        dialog_full.append(f"**Bob says:** {response2}")
        dialog_anna.append(f"**Bob says:** {response2}")
        dialog_bob.append(f"**Bob says:** {response2}")

        # Prepare the next message for Model 1
        message = response2

    return dialog_full, dialog_anna, dialog_bob

def save_dialog_to_md(dialog, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write("# Dialog between Anna and Bob\n\n")
        for line in dialog:
            file.write(f"{line}\n\n")

# Example usage of the function
num_turns = 1
dialog_full, dialog_anna, dialog_bob = dialog_between_models(num_turns)
save_dialog_to_md(dialog_full, 'dialog_full.md')
save_dialog_to_md(dialog_anna, 'dialog_anna.md')
save_dialog_to_md(dialog_bob, 'dialog_bob.md')