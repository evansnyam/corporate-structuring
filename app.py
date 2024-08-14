import streamlit as st

# Business structures data
structures = [
    {"name": "Sole Proprietorship", "owners": "1", "liability": "Personal", "management": "Owner makes all decisions", "makeProfits": "Yes", "profitSharing": "Owner keeps all profits", "funding": "Personal funds", "easeOfSetup": 1, "publicFundraising": "Not allowed"},
    {"name": "General Partnership", "owners": "More than one", "liability": "Shared", "management": "Partners share decisions", "makeProfits": "Yes", "profitSharing": "Shared equally", "funding": "Partners' contributions", "easeOfSetup": 2, "publicFundraising": "Not allowed"},
    {"name": "Limited Liability Partnership (LLP)", "owners": "More than one", "liability": "Limited", "management": "Partners share decisions", "makeProfits": "Yes", "profitSharing": "According to agreement", "funding": "Partners' contributions", "easeOfSetup": 3, "publicFundraising": "Not allowed"},
    {"name": "Limited Liability Company (LLC)", "owners": "More than one", "liability": "Limited", "management": "Owner or managers", "makeProfits": "Yes", "profitSharing": "According to agreement", "funding": "Personal funds and loans", "easeOfSetup": 3, "publicFundraising": "Not allowed"},
    {"name": "S Corporation (S-Corp)", "owners": "One or more", "liability": "Limited", "management": "Board of directors", "makeProfits": "Yes", "profitSharing": "Based on shares", "funding": "Sale of shares", "easeOfSetup": 4, "publicFundraising": "Allowed"},
    {"name": "C Corporation (C-Corp)", "owners": "One or more", "liability": "Limited", "management": "Board of directors", "makeProfits": "Yes", "profitSharing": "Based on shares", "funding": "Sale of stocks", "easeOfSetup": 5, "publicFundraising": "Allowed"},
    {"name": "Cooperative", "owners": "More than one", "liability": "Limited", "management": "Democratic", "makeProfits": "Yes", "profitSharing": "Based on usage", "funding": "Members' contributions and loans", "easeOfSetup": 4, "publicFundraising": "Allowed"},
    {"name": "Non-Profit", "owners": "More than one", "liability": "Limited", "management": "Board of directors", "makeProfits": "No", "profitSharing": "None", "funding": "Donations and grants", "easeOfSetup": 5, "publicFundraising": "Allowed"}
]

# Streamlit UI
st.title('Find the Best Business Structure for You')

st.write(
    "To help you choose the best business structure, please provide some details about your needs. "
    "We'll recommend the options that best fit your situation."
)

# User input
owners = st.selectbox('How many people will own the business?', ['1', 'More than one'])
liability = st.selectbox('How do you want to handle legal responsibility for debts and actions?', ['Personal', 'Shared', 'Limited'])
management = st.selectbox('How will decisions be made?', ['Owner makes all decisions', 'Partners share decisions', 'Owner or managers', 'Board of directors', 'Democratic'])
makeProfits = st.selectbox('Will your business make profits?', ['Yes', 'No'])
profitSharing = st.selectbox('How will profits be shared?', ['Owner keeps all profits', 'Shared equally', 'According to agreement', 'Based on usage', 'None'])
funding = st.selectbox('How will you get funds for the business?', ['Personal funds', 'Partners\' contributions', 'Personal funds and loans', 'Sale of shares/stocks', 'Donations and grants'])
easeOfSetup = st.slider('How easy do you want it to be to set up?', 1, 5, 3)
publicFundraising = st.selectbox('Do you want to raise money from the public?', ['Allowed', 'Not allowed'])

def recommend_structure():
    # Recommend based on user input
    best_structures = [s for s in structures if
        s['owners'] == owners and
        s['liability'] == liability and
        s['management'] == management and
        s['makeProfits'] == makeProfits and
        s['profitSharing'] == profitSharing and
        s['funding'] == funding and
        s['easeOfSetup'] <= easeOfSetup and
        s['publicFundraising'] == publicFundraising
    ]
    return best_structures

if st.button('Find My Best Business Structure'):
    results = recommend_structure()
    if results:
        st.write('### Recommended Business Structures:')
        for structure in results:
            st.write(f"- **{structure['name']}**: {structure['management']} with {structure['liability']} liability. Profits: {structure['makeProfits']}. Funding: {structure['funding']}. Ease of setup: {structure['easeOfSetup']}.")
    else:
        st.write("No matching business structure found. Try adjusting your preferences.")
