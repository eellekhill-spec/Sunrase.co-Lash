[README.md](https://github.com/user-attachments/files/24951178/README.md)
# Sunrae's Beauty Bar & Spa - Chatbot

A Streamlit-based chatbot for Sunrae's Beauty Bar & Spa in Nashville, TN. This chatbot helps customers get information about services, pricing, booking policies, and answers common questions.

## Features

- 💬 Interactive chat interface
- 📋 Service and pricing information
- 📅 Appointment booking assistance
- 💳 Policy information (deposits, cancellations, etc.)
- ❓ FAQ database
- 📱 Mobile-responsive design
- ✨ Customizable branding

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup Steps

1. **Install Python dependencies:**
```bash
pip install -r requirements.txt
```

2. **Run the application:**
```bash
streamlit run sunraes_chatbot.py
```

3. **Access the chatbot:**
   - The app will open automatically in your browser
   - Or navigate to: `http://localhost:8501`

## Customization Guide

### 🔧 IMPORTANT: Update Business Information

Before deploying, you MUST update the following sections in `sunraes_chatbot.py`:

#### 1. Business Contact Information (Lines 7-18)
```python
BUSINESS_INFO = {
    "name": "Sunrae's Beauty Bar & Spa",
    "phone": "(216) 278-8833",  # ← UPDATE
    "location": "Cleveland, OH 44128",  # ← UPDATE with full address
    "website": "sunraesbeautybar.as.me",
    "booking_url": "https://sunraesbeauty.as.me/schedule/975618b2",
    "hours": {
        "Monday-Sunday": "By Appointment"  # ← UPDATE with actual hours
    }
}
```

#### 2. Services and Pricing (Lines 21-87)
Replace all "$XX" placeholders with actual prices. Example:

```python
"Classic Lashes": {
    "Full Set": "$150",  # ← UPDATE
    "Fill (2-3 weeks)": "$75",  # ← UPDATE
    "description": "Natural look with one lash per natural lash"
}
```

Add or remove services as needed.

#### 3. Policies (Lines 90-124)
Update deposit requirements, cancellation policies, etc.:

```python
"deposit": {
    "required": True,  # ← UPDATE (True/False)
    "amount": "$25",  # ← UPDATE
    "refundable": False,  # ← UPDATE
    "details": "..."  # ← UPDATE with your policy
}
```

#### 4. Add Your Logo (Line 234)
Replace the placeholder image URL with your actual logo:

```python
st.image("YOUR_LOGO_URL_HERE", use_container_width=True)
```

Or use a local file:
```python
st.image("logo.png", use_container_width=True)
```

## File Structure

```
.
├── sunraes_chatbot.py      # Main chatbot application
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## Deployment Options

### Option 1: Streamlit Community Cloud (Recommended - FREE)

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Sign in with GitHub
4. Deploy your app with one click!

### Option 2: Local Network

Run on your local computer and share on your network:
```bash
streamlit run sunraes_chatbot.py --server.address 0.0.0.0
```

### Option 3: Heroku/AWS/Other Cloud Providers

Follow their respective Streamlit deployment guides.

## Integration with Existing App

To integrate this chatbot into an existing Streamlit app:

```python
import streamlit as st
from sunraes_chatbot import main as chatbot_main

# Your existing app code...

# Add chatbot page
if st.sidebar.button("💬 Chat Support"):
    chatbot_main()
```

Or create a multi-page app:
```
your_app/
├── main_app.py
└── pages/
    └── chatbot.py  # Copy sunraes_chatbot.py here
```

## Customization Tips

### Change Colors
Modify the CSS in the `main()` function (around line 227):

```python
st.markdown("""
    <style>
    .main {
        background-color: #YOUR_COLOR;  # Change background
    }
    </style>
""", unsafe_allow_html=True)
```

### Add New FAQ
Add to the `FAQ` dictionary (lines 127-150):

```python
FAQ = {
    "Your question here?": "Your answer here",
    # Add more...
}
```

### Modify Response Logic
Update the `get_response()` function (lines 158-333) to add new conversation patterns.

## Features Breakdown

### What the Chatbot Can Answer:
- ✅ Service descriptions and pricing
- ✅ Booking procedures and links
- ✅ Location and hours
- ✅ Deposit and payment policies
- ✅ Cancellation policies
- ✅ Lash care instructions
- ✅ Common questions (via FAQ)
- ✅ Contact information

### Conversation Patterns Recognized:
- Greetings (hi, hello, hey)
- Service inquiries (lash extensions, brow services)
- Pricing questions (how much, cost, price)
- Booking requests (book, appointment, schedule)
- Policy questions (deposit, cancel, late)
- Contact requests (phone, call, location)

## Troubleshooting

### App won't start
```bash
# Make sure Streamlit is installed
pip install --upgrade streamlit

# Check Python version (need 3.8+)
python --version
```

### Port already in use
```bash
# Use a different port
streamlit run sunraes_chatbot.py --server.port 8502
```

### Styling not showing
- Clear browser cache
- Hard refresh (Ctrl+F5 or Cmd+Shift+R)

## Support

For questions about the chatbot code:
- Review the inline comments in `sunraes_chatbot.py`
- Check [Streamlit documentation](https://docs.streamlit.io)

For business-specific updates:
- Update the dictionaries at the top of the file
- Test locally before deploying

## Future Enhancements

Potential additions you could make:
- 🤖 AI-powered responses (integrate with OpenAI API)
- 📧 Email notification system
- 📊 Analytics dashboard
- 🌐 Multi-language support
- 📸 Gallery of lash work
- ⭐ Review/testimonial display
- 🎁 Promotion announcements

## License

This chatbot is created for Sunrae's Beauty Bar & Spa. Modify as needed for your business use.

---

**Need help?** Check the Streamlit documentation or contact your developer.

**Ready to go live?** Make sure all placeholder information is updated!
