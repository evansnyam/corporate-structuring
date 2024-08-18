import streamlit as st

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
owners = st.selectbox('How many people will own the business?', ['One person', 'Two or more people'])

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

liability = st.selectbox('How do you want to handle legal responsibility for debts and actions?', [
    'You are personally responsible for all debts and actions of the business', 
    'Responsibility is shared among partners', 
    'Your liability is limited to the amount you invest in the business'
])

management = st.selectbox('How will decisions be made?', [
    'One person makes all decisions', 
    'Decisions are shared among partners', 
    'Decisions are made by managers or a board of directors', 
    'Decisions are made democratically by all members'
])

# Rephrased funding question
funding = st.selectbox('Will you raise funds by selling shares or stocks?', [
    'No, only personal funds will be used', 
    'No, funds will be contributed by partners', 
    'Yes, by selling shares', 
    'Yes, by selling stocks', 
    'No, funds will come from donations and grants'
])

# Updated scoring system
def recommend_structure():
    scores = []
    
    for s in structures:
        score = 0
        
        # Critical criteria with higher weight
        if (owners == 'One person' and '1' in s['owners']) or (owners == 'Two or more people' and 'More than one' in s['owners']):
            score += 2  # Higher weight for ownership match
        
        if liability == 'You are personally responsible for all debts and actions of the business' and s['liability'][0] == 'Personal':
            score += 3
        elif liability == 'Responsibility is shared among partners' and s['liability'][0] == 'Shared':
            score += 3
        elif liability == 'Your liability is limited to the amount you invest in the business' and s['liability'][0] == 'Limited':
            score += 3
        
        # Increase weight for profit-related match
        if s['makeProfits'] == makeProfits:
            score += 5  # Increased points for matching profit criterion
        
        # Only score profit-sharing and public fundraising if profits are being made
        if makeProfits == 'Yes':
            if s['profitSharing'] == profitSharing:
                score += 2
            
            if s['publicFundraising'] == publicFundraising:
                score += 1
        
        # Other criteria
        if s['management'] == management:
            score += 2
        
        if s['funding'] == funding:
            score += 1
        
        s['score'] = score
    
    # Sort structures by score and return top recommendation
    recommended = sorted(structures, key=lambda x: x['score'], reverse=True)
    return recommended

# Detailed output with call-to-action
def display_recommendation():
    results = recommend_structure()
    if results:
        top_structure = results[0]  # Get the top recommendation
        st.write(f"### Recommended Business Structure: **{top_structure['name']}**")
        
        # Descriptions of each business structure
        descriptions = {
            'Sole Proprietorship': {
                'advantages': [
                    'Simple and inexpensive to establish and operate.',
                    'Owner has full control over all business decisions.',
                    'All profits go directly to the owner.'
                ],
                'disadvantages': [
                    'Owner is personally liable for all business debts and actions.',
                    'Limited ability to raise funds or attract investors.'
                ]
            },
            'General Partnership': {
                'advantages': [
                    'Simple to establish with shared decision-making among partners.',
                    'Combined resources and expertise of partners.',
                    'Profits are shared among partners.'
                ],
                'disadvantages': [
                    'Partners are jointly personally liable for all business debts and actions.',
                    'Potential for conflicts between partners.'
                ]
            },
            'Limited Liability Partnership (LLP)': {
                'advantages': [
                    'Limited liability protection for partners.',
                    'Flexibility in management and profit-sharing arrangements.',
                    'Each partner’s personal liability is limited to their investment.'
                ],
                'disadvantages': [
                    'More complex and costly to establish compared to a general partnership.',
                    'Potential for limited access to capital and financing.'
                ]
            },
            'Limited Liability Company (LLC)': {
                'advantages': [
                    'Limited liability protection for owners.',
                    'Flexible management structure and profit distribution.',
                    'Pass-through taxation or option for corporate taxation.'
                ],
                'disadvantages': [
                    'More complex and costly to establish compared to a sole proprietorship or partnership.',
                    'State laws regarding LLCs vary and can be complex.'
                ]
            },
            'S Corporation (S-Corp)': {
                'advantages': [
                    'Limited liability protection for owners.',
                    'Pass-through taxation avoiding double taxation.',
                    'Ability to raise funds through the sale of shares.'
                ],
                'disadvantages': [
                    'Restrictions on the number and type of shareholders.',
                    'More complex and costly to establish and maintain.'
                ]
            },
            'C Corporation (C-Corp)': {
                'advantages': [
                    'Limited liability protection for owners.',
                    'Unlimited potential for raising funds through stock sales.',
                    'Ability to attract investors with stock options.'
                ],
                'disadvantages': [
                    'Double taxation on profits (corporate and personal level).',
                    'More complex and costly to establish and maintain.'
                ]
            },
            'Cooperative': {
                'advantages': [
                    'Democratic management by members.',
                    'Profits are distributed based on member participation.',
                    'Limited liability protection for members.'
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
