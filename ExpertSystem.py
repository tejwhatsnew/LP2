QUESTIONS = [
    'Do you have a cough?',
    'Do you have a sore throat?',
    'Do you have a fever?',
    'Are you noticing any unexplained excessive sweating?',
    'Do you have an itchy throat?',
    'Do you have a runny nose?',
    'Do you have a stuffy nose?',
    'Do you have a headache?',
    'Do you feel tired without actually exhausting yourself?'
]

THRESHOLD = {
    'Mild': 30,
    'Severe': 50,
    'Extreme': 75
}

def validate_input(prompt, valid_inputs):
    while True:
        user_input = input(prompt).lower()
        if user_input in valid_inputs:
            return user_input
        print('Invalid input. Please enter a valid option.')

def expert_system(questions, threshold):
    score = 0

    for question in questions:
        print(question)
        ans = validate_input('(Y/N): ', ['y', 'n'])

        if ans == 'y':
            print('On a scale of 1-10, how bad is it?')
            ip = validate_input('(1-10): ', [str(i) for i in range(1, 11)])
            score += int(ip)

    print()

    if score >= threshold['Extreme']:
        print('You are showing symptoms of EXTREME COVID-19.')
        print('Please call +91 8928184137 immediately for immediate assistance.')
        print('Based on your symptoms, you will need immediate hospitalization.')
    elif score >= threshold['Severe']:
        print('Based on your answers, you are showing symptoms of SEVERE COVID-19.')
        print('You are advised to contact a COVID-19 specialist ASAP.')
        print('You are prescribed with Favipriavir, Dolo 650 / Crocin 500, Paracetamol, Brufane.')
        print('Also conduct a COVID-19 Lab Test ASAP as this might be a false positive.')
        print('Lab Testing: https://www.metropolisindia.com/parameter/pune/covid-19-rt-pcr-test')
    elif score >= threshold['Mild']:
        print('Based on your answers, you are showing symptoms of VERY MILD COVID-19.')
        print('Please isolate yourself immediately on a precautionary basis.')
        print('As this has a possibility of being a false positive, please consider testing yourself.')
        print('At-home testing using Self-Testing kits is recommended, but you can get Lab Tests as well.')
        print('Self-testing: https://www.flipkart.com/mylab-coviself-covid-19-rapid-antigen-test-kit/p/itm4d34ea09cad97')
        print('Lab Testing: https://www.metropolisindia.com/parameter/pune/covid-19-rt-pcr-test')
    else:
        print('You are showing NO symptoms of COVID-19.')
        print('This might be a false negative. If you feel unsure, please get tested.')
        print('As this has a possibility of being a false negative, please consider testing yourself.')
        print('At-home testing using Self-Testing kits is recommended.')
        print('Self-testing: https://www.flipkart.com/mylab-coviself-covid-19-rapid-antigen-test-kit/p/itm4d34ea09cad97')

    print('\nFor any further queries, visit: https://www.aarogyasetu.gov.in/')

print('\n\n\t\tWelcome To The COVID-19 EXPERT SYSTEM\n')
print('\tNote: Please answer the following questions very honestly.\n\n')
expert_system(QUESTIONS, THRESHOLD)
