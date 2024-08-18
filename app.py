import streamlit as st

# Updated list of countries
countries = [
    "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda",
    "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "The Bahamas", 
    "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin",
    "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei",
    "Bulgaria", "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon",
    "Canada", "Central African Republic", "Chad", "Chile", "China", "Colombia",
    "Comoros", "Congo, Democratic Republic of the", "Congo, Republic of the",
    "Costa Rica", "Côte d’Ivoire", "Croatia", "Cuba", "Cyprus", "Czech Republic",
    "Denmark", "Djibouti", "Dominica", "Dominican Republic", "East Timor (Timor-Leste)",
    "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia",
    "Eswatini", "Ethiopia", "Fiji", "Finland", "France", "Gabon", "The Gambia",
    "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea",
    "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", "India",
    "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan",
    "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Korea, North", "Korea, South",
    "Kosovo", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho",
    "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar",
    "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands",
    "Mauritania", "Mauritius", "Mexico", "Micronesia, Federated States of", "Moldova",
    "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar (Burma)",
    "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger",
    "Nigeria", "North Macedonia", "Norway", "Oman", "Pakistan", "Palau", "Panama",
    "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal",
    "Qatar", "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia",
    "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe",
    "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore",
    "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "Spain",
    "Sri Lanka", "Sudan", "Sudan, South", "Suriname", "Sweden", "Switzerland", "Syria",
    "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Togo", "Tonga", "Trinidad and Tobago",
    "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates",
    "United Kingdom", "United States", "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City",
    "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"
]

# Business structures data
structures = [
    {"name": "Sole Proprietorship", "owners": ["1"], "liability": ["Personal"], "management": "Owner makes all decisions", "makeProfits": "Yes", "profitSharing": "Owner keeps all profits", "funding": "Personal funds", "publicFundraising": "Not allowed"},
    {"name": "General Partnership", "owners": ["More than one"], "liability": ["Shared"], "management": "Partners share decisions", "makeProfits": "Yes", "profitSharing": "Shared equally", "funding": "Partners' contributions", "publicFundraising": "Not allowed"},
    {"name": "Limited Liability Partnership (LLP)", "owners": ["More than one"], "liability": ["Limited"], "management": "Partners share decisions", "makeProfits": "Yes", "profitSharing": "According to agreement", "funding": "Partners' contributions", "publicFundraising": "Not allowed"},
    {"name": "Limited Liability Company (LLC)", "owners": ["One or more"], "liability": ["Limited"], "management": "Owner or managers", "makeProfits": "Yes", "profitSharing": "According to agreement", "funding": "Personal funds and loans", "publicFundraising": "Not allowed"},
    {"name": "S Corporation (S-Corp)", "owners": ["One or more"], "liability": ["Limited"], "management": "Board of directors", "makeProfits": "Yes", "profitSharing": "Based on shares", "funding": "Sale of shares", "publicFundraising": "Allowed"},
    {"name": "C Corporation (C-Corp)", "owners": ["One or more"], "liability": ["Limited"], "management": "Board of directors", "makeProfits": "Yes", "profitSharing": "Based on shares", "funding": "Sale of stocks", "publicFundraising": "Allowed"},
    {"name": "Cooperative", "owners": ["More than one"], "liability": ["Limited"], "management": "Democratic", "makeProfits": "Yes", "profitSharing": "Based on usage", "funding": "Members' contributions and loans", "publicFundraising": "Allowed"},
    {"name": "Non-Profit", "owners": ["More than one"], "liability": ["Limited"], "management": "Board of directors", "makeProfits": "No", "profitSharing": "None", "funding": "Donations and grants", "publicFundraising": "Allowed"}
]

# Streamlit UI
st.title('Find the Best Business Structure for You')

st.write(
    "To help you choose the best business structure, please provide some details about your needs. "
    "We'll recommend the options that best fit your situation."
)

# User input
country = st.selectbox('Which country will your business operate in?', countries)
business_description = st.text_input('What type of business are you starting? (e.g., salon, law firm)')

# Ownership and other details
owners = st.selectbox('How many people will own the business?', ['One person', 'Two or more people'])

# Dynamic options based on ownership
if owners == 'One person':
    management_options = ['One person makes all decisions']
    funding_options = ['Only personal funds will be used']
    liability_options = ['You are personally responsible for all debts and actions of the business']
else:
    management_options = ['Partners share decisions', 'Decisions are made by managers or a board of directors', 'Decisions are made democratically by all members']
    funding_options = ['Partners\' contributions', 'Personal funds and loans', 'Members\' contributions and loans']
    liability_options = ['Responsibility is shared among partners', 'Your liability is limited to the amount you invest in the business']

# Profit-related question
makeProfits = st.selectbox('Will your business make profits?', ['Yes', 'No'])

if makeProfits == 'Yes':
    # Display profit sharing and public fundraising questions if the business will make profits
    profitSharing = st.selectbox('How will profits be shared?', [
        'One person keeps all profits', 
        'Profits are shared equally among owners', 
        'Profits are distributed based on an agreement', 
        'Profits are shared based on usage or participation'
    ])
    publicFundraising = st.selectbox('Do you want to raise money from the public?', ['Yes', 'No'])
    publicFundraising = "Allowed" if publicFundraising == "Yes" else "Not allowed"
else:
    # Hide profit sharing and public fundraising questions if the business will not make profits
    profitSharing = 'None'
    publicFundraising = 'Not allowed'

liability = st.selectbox('How do you want to handle legal responsibility for debts and actions?', liability_options)

management = st.selectbox('How will decisions be made?', management_options)

# Updated funding options based on ownership
funding = st.selectbox('Will you raise funds by selling shares or stocks?', funding_options)

# Updated scoring system
def recommend_structure():
    scores = []
    
    for s in structures:
        score = 0
        
        if s["owners"][0] == "One person" and owners == "One person":
            score += 1
        elif s["owners"][0] == "More than one" and owners == "Two or more people":
            score += 1
        
        if s["management"] == management:
            score += 1
        
        if s["funding"] == funding:
            score += 1
        
        if s["liability"][0] in liability:
            score += 1
        
        if makeProfits == "Yes" and s["makeProfits"] == "Yes":
            score += 1
        elif makeProfits == "No" and s["makeProfits"] == "No":
            score += 1
        
        if profitSharing in s["profitSharing"]:
            score += 1
        
        if publicFundraising == s["publicFundraising"]:
            score += 1
        
        scores.append({"name": s["name"], "score": score, "liability": s["liability"], "management": s["management"], "funding": s["funding"]})
    
    scores.sort(key=lambda x: x["score"], reverse=True)
    return scores

# Display the recommendation
def display_recommendation():
    results = recommend_structure()
    
    if results:
        top_structure = results[0]
        
        st.write(f"### Recommended Business Structure: {top_structure['name']}")
        
        # Show detailed descriptions
        descriptions = {
            'Sole Proprietorship': {
                'advantages': [
                    'Simple to establish and operate.',
                    'Owner keeps all profits.'
                ],
                'disadvantages': [
                    'Owner is personally liable for all debts and actions.',
                    'Limited ability to raise funds.'
                ]
            },
            'General Partnership': {
                'advantages': [
                    'Simple to establish.',
                    'Shared responsibility among partners.'
                ],
                'disadvantages': [
                    'Partners are personally liable for debts and actions.',
                    'Disagreements between partners can affect the business.'
                ]
            },
            'Limited Liability Partnership (LLP)': {
                'advantages': [
                    'Limited liability for partners.',
                    'Flexibility in management.'
                ],
                'disadvantages': [
                    'More complex to establish than a general partnership.',
                    'Potential for disagreements among partners.'
                ]
            },
            'Limited Liability Company (LLC)': {
                'advantages': [
                    'Limited liability for owners.',
                    'Flexible management structure.'
                ],
                'disadvantages': [
                    'More complex and costly to establish and operate.'
                ]
            },
            'S Corporation (S-Corp)': {
                'advantages': [
                    'Limited liability protection for owners.',
                    'Ability to raise funds through stock sales.'
                ],
                'disadvantages': [
                    'Strict requirements and regulations.',
                    'Limited to 100 shareholders.'
                ]
            },
            'C Corporation (C-Corp)': {
                'advantages': [
                    'Limited liability protection for owners.',
                    'Ability to raise substantial funds through stock sales.',
                    'Perpetual existence.'
                ],
                'disadvantages': [
                    'Double taxation (corporate tax and dividend tax).',
                    'More complex and costly to establish and operate.'
                ]
            },
            'Cooperative': {
                'advantages': [
                    'Democratic management structure.',
                    'Limited liability for members.',
                    'Ability to attract funds through membership contributions and loans.'
                ],
                'disadvantages': [
                    'Decision-making can be slower and more complex.',
                    'Limited ability to raise capital from outside sources.'
                ]
            },
            'Non-Profit': {
                'advantages': [
                    'Exempt from paying income taxes.',
                    'Ability to receive donations and grants.',
                    'Limited liability protection for directors and officers.'
                ],
                'disadvantages': [
                    'Profits cannot be distributed to owners or members.',
                    'Strict compliance and reporting requirements.'
                ]
            }
        }
        
        st.write("### Description")
        st.write("**Advantages:**")
        for advantage in descriptions[top_structure['name']]['advantages']:
            st.write(f"- {advantage}")
        
        st.write("**Disadvantages:**")
        for disadvantage in descriptions[top_structure['name']]['disadvantages']:
            st.write(f"- {disadvantage}")
        
        st.write(f"This structure is suitable based on your answers regarding ownership, liability, management, profits, and other criteria. You can start with this and adjust as needed.")

        # Call-to-action with option to review alternatives
        if st.button('See More Options'):
            st.write("### Alternative Business Structures")
            for structure in results[1:]:
                st.write(f"**{structure['name']}** (Score: {structure['score']})")
                st.write(f"- Liability: {structure['liability'][0]}")
                st.write(f"- Management: {structure['management']}")
                st.write("---")
    else:
        st.write("Sorry, we couldn't find a suitable business structure for your inputs. Please try different options.")

# Display the recommendation
display_recommendation()
