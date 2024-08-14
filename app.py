import streamlit as st

# Business structures data
structures = [
    {"name": "Sole Proprietorship", "owners": ["1"], "liability": ["Personal"], "management": "Owner makes all decisions", "makeProfits": "Yes", "profitSharing": "Owner keeps all profits", "funding": "Personal funds", "easeOfSetup": 1, "publicFundraising": "Not allowed"},
    {"name": "General Partnership", "owners": ["More than one"], "liability": ["Shared"], "management": "Partners share decisions", "makeProfits": "Yes", "profitSharing": "Shared equally", "funding": "Partners' contributions", "easeOfSetup": 2, "publicFundraising": "Not allowed"},
    {"name": "Limited Liability Partnership (LLP)", "owners": ["More than one"], "liability": ["Limited"], "management": "Partners share decisions", "makeProfits": "Yes", "profitSharing": "According to agreement", "funding": "Partners' contributions", "easeOfSetup": 3, "publicFundraising": "Not allowed"},
    {"name": "Limited Liability Company (LLC)", "owners": ["One or more"], "liability": ["Limited"], "management": "Owner or managers", "makeProfits": "Yes", "profitSharing": "According to agreement", "funding": "Personal funds and loans", "easeOfSetup": 3, "publicFundraising": "Not allowed"},
    {"name": "S Corporation (S-Corp)", "owners": ["One or more"], "liability": ["Limited"], "management": "Board of directors", "makeProfits": "Yes", "profitSharing": "Based on shares", "funding": "Sale of shares", "easeOfSetup": 4, "publicFundraising": "Allowed"},
    {"name": "C Corporation (C-Corp)", "owners": ["One or more"], "liability": ["Limited"], "management": "Board of directors", "makeProfits": "Yes", "profitSharing": "Based on shares", "funding": "Sale of stocks", "easeOfSetup": 5, "publicFundraising": "Allowed"},
    {"name": "Cooperative", "owners": ["More than one"], "liability": ["Limited"], "management": "Democratic", "makeProfits": "Yes", "profitSharing": "Based on usage", "funding": "Members' contributions and loans", "easeOfSetup": 4, "publicFundraising": "Allowed"},
    {"name": "Non-Profit", "owners": ["More than one"], "liability": ["Limited"], "management": "Board of directors", "makeProfits": "No", "profitSharing": "None", "funding": "Donations and grants", "easeOfSetup": 5, "publicFundraising": "Allowed"}
]

# Streamlit UI
st.title('Find the Best Business Structure for You')

st.write(
    "To help you choose the best business structure, please provide some details about your needs. "
    "We'll recommend the options that best fit your situation."
)

# User input
owners = st.selectbox('How many people will own the business?', ['One person', 'Two or more people'])
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
makeProfits = st.selectbox('Will your business make profits?', ['Yes', 'No'])
profitSharing = st.selectbox('How will profits be shared?', [
    'One person keeps all profits', 
    'Profits are shared equally among owners', 
    'Profits are distributed based on an agreement', 
    'Profits are shared based on usage or participation', 
    'No profits are generated or shared'
])
funding = st.selectbox('How will you get funds for the business?', [
    'Only personal funds', 
    'Contributions from partners', 
    'Personal funds and loans', 
    'Sale of shares or stocks', 
    'Donations and grants'
])
easeOfSetup = st.slider('How easy do you want it to be to set up?', 1, 5, 3)
publicFundraising = st.selectbox('Do you want to raise money from the public?', ['Allowed', 'Not allowed'])

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
        
        # Other criteria
        if s['management'] == management:
            score += 2
        
        if s['makeProfits'] == makeProfits:
            score += 2
        
        if s['profitSharing'] == profitSharing:
            score += 2
        
        if s['funding'] == funding:
            score += 1
        
        if s['easeOfSetup'] <= easeOfSetup:
            score += 1
        
        if s['publicFundraising'] == publicFundraising:
            score += 1
        
        s['score'] = score
    
    # Sort structures by score and return top recommendations
    recommended = sorted(structures, key=lambda x: x['score'], reverse=True)
    return recommended

if st.button('Find My Best Business Structure'):
    results = recommend_structure()
    if results:
        st.write('### Recommended Business Structures:')
        for structure in results:
            st.write(f"- **{structure['name']}**: {structure['management']} with {structure['liability']} liability. Profits: {structure['makeProfits']}. Funding: {structure['funding']}. Ease of setup: {structure['easeOfSetup']}. Score: {structure['score']}")
    else:
        st.write("No matching business structure found. Try adjusting your preferences.")
