import streamlit as st
from datetime import datetime
import json
import os

def load_config():
    """Load configuration from JSON file if it exists, otherwise use defaults"""
    config_file = "config.json"
    
    if os.path.exists(config_file):
        with open(config_file, 'r') as f:
            return json.load(f)
    else:
        # Default configuration
        return {
            "business_info": {
                "name": "Sunrae's Beauty Bar & Spa",
                "phone": "UPDATE_PHONE",
                "location": "Nashville, TN",
                "website": "sunraesbeauty.as.me",
                "booking_url": "https://sunraesbeauty.as.me/schedule/975618b2",
                "hours": {"Monday-Sunday": "By Appointment"}
            },
            "services": {
                "lash_extensions": {
                    "Classic Lashes Full Set": "UPDATE_PRICE",
                    "Classic Lashes Fill": "UPDATE_PRICE"
                }
            },
            "policies": {
                "deposit": {
                    "required": True,
                    "amount": "UPDATE_AMOUNT",
                    "refundable": False,
                    "details": "UPDATE_POLICY"
                },
                "cancellation": {
                    "notice_hours": 24,
                    "policy_text": "UPDATE_POLICY"
                },
                "late_arrival": {
                    "grace_period_minutes": 15,
                    "policy_text": "UPDATE_POLICY"
                },
                "payment_methods": ["Credit Cards", "Debit Cards", "Cash"]
            },
            "faq": {
                "How long do lash extensions last?": "UPDATE_ANSWER"
            }
        }

# Load configuration
CONFIG = load_config()

def format_price(price):
    """Format price for display"""
    if isinstance(price, (int, float)):
        return f"${price}"
    return price

def initialize_session_state():
    """Initialize session state variables"""
    if 'messages' not in st.session_state:
        business_name = CONFIG['business_info']['name']
        st.session_state.messages = [{
            "role": "assistant",
            "content": f"Hello! Welcome to {business_name}! 💅✨\n\nI'm here to help you with:\n- Information about our lash and beauty services\n- Pricing and appointment details\n- Booking policies and aftercare tips\n- Answering your questions\n\nWhat can I help you with today?"
        }]

def get_response(user_message):
    """Generate chatbot response based on user input"""
    message_lower = user_message.lower()
    business_info = CONFIG['business_info']
    
    # Greeting responses
    if any(greeting in message_lower for greeting in ['hello', 'hi', 'hey', 'good morning', 'good afternoon', 'good evening']):
        return f"Hello! Thanks for reaching out to {business_info['name']}! How can I assist you today? I can tell you about our services, pricing, appointment policies, or answer any questions you have. 😊"
    
    # Hours and location
    if any(word in message_lower for word in ['hours', 'open', 'when are you open', 'what time']):
        hours_text = "\n".join([f"{day}: {time}" for day, time in business_info['hours'].items()])
        return f"📍 We're located in {business_info['location']}\n\n⏰ Our hours:\n{hours_text}\n\nWe recommend booking in advance! Would you like our booking link?"
    
    if any(word in message_lower for word in ['location', 'address', 'where are you', 'where located']):
        response = f"📍 We're located at {business_info['location']}"
        if 'full_address' in business_info:
            response = f"📍 {business_info['full_address']}"
        response += f"\n\nYou can call us at {business_info['phone']} for directions or questions!"
        return response
    
    # Booking
    if any(word in message_lower for word in ['book', 'appointment', 'schedule', 'reservation', 'how do i book']):
        return f"Great! You can book your appointment online here:\n🔗 {business_info['booking_url']}\n\nOr call us at {business_info['phone']}\n\n💡 Tip: We recommend booking 1-2 weeks in advance, especially for weekends!"
    
    # Contact
    if any(word in message_lower for word in ['phone', 'call', 'contact', 'reach', 'email']):
        response = f"📞 Phone: {business_info['phone']}\n🌐 Website: {business_info['website']}\n📍 Location: {business_info['location']}"
        if 'email' in business_info:
            response += f"\n📧 Email: {business_info['email']}"
        if 'instagram' in business_info:
            response += f"\n📱 Instagram: {business_info['instagram']}"
        response += "\n\nFeel free to call or text us with any questions!"
        return response
    
    # Pricing - Show all services
    if 'price' in message_lower or 'cost' in message_lower or 'how much' in message_lower or 'pricing' in message_lower:
        response = "💰 **Our Services & Pricing:**\n\n"
        
        services = CONFIG.get('services', {})
        
        if 'lash_extensions' in services:
            response += "**Lash Extensions**\n"
            for service, price in services['lash_extensions'].items():
                response += f"  • {service}: {format_price(price)}\n"
            response += "\n"
        
        if 'lash_services' in services:
            response += "**Lash Services**\n"
            for service, price in services['lash_services'].items():
                response += f"  • {service}: {format_price(price)}\n"
            response += "\n"
        
        if 'brow_services' in services:
            response += "**Brow Services**\n"
            for service, price in services['brow_services'].items():
                response += f"  • {service}: {format_price(price)}\n"
            response += "\n"
        
        if 'facial_services' in services:
            response += "**Facial & Skin Services**\n"
            for service, price in services['facial_services'].items():
                response += f"  • {service}: {format_price(price)}\n"
            response += "\n"
        
        response += "Would you like more details about any specific service?"
        return response
    
    # Deposit policy
    if any(word in message_lower for word in ['deposit', 'down payment', 'payment required']):
        deposit_info = CONFIG['policies']['deposit']
        response = f"💳 **Deposit Policy:**\n{deposit_info['details']}\n\n"
        payment_methods = CONFIG['policies'].get('payment_methods', [])
        if payment_methods:
            response += f"We accept: {', '.join(payment_methods)}"
        return response
    
    # Cancellation policy
    if any(word in message_lower for word in ['cancel', 'reschedule', 'change appointment', 'cancellation']):
        cancel_policy = CONFIG['policies']['cancellation']
        return f"📅 **Cancellation & Rescheduling:**\n{cancel_policy['policy_text']}\n\nWe understand life happens! Just give us a call at {business_info['phone']} if you need to make changes."
    
    # Late policy
    if any(word in message_lower for word in ['late', 'running behind', 'running late', 'delay']):
        late_policy = CONFIG['policies']['late_arrival']
        return f"⏰ **Late Arrival Policy:**\n{late_policy['policy_text']}\n\nPlease call us at {business_info['phone']} if you're running late!"
    
    # Payment methods
    if any(word in message_lower for word in ['payment', 'pay', 'credit card', 'cash', 'venmo']):
        payment_methods = CONFIG['policies'].get('payment_methods', [])
        deposit_info = CONFIG['policies']['deposit']
        return f"💳 **Payment Information:**\n\nWe accept: {', '.join(payment_methods)}\n\n{deposit_info['details']}"
    
    # Lash extensions general
    if 'lash extension' in message_lower or 'eyelash extension' in message_lower:
        extensions = CONFIG['services'].get('lash_extensions', {})
        response = "✨ **Lash Extensions at Sunrae's:**\n\n"
        response += "We offer several lash styles to fit your look:\n"
        
        # Extract unique style names
        styles = set()
        for service_name in extensions.keys():
            if 'Full Set' in service_name:
                style = service_name.replace(' Full Set', '')
                styles.add(style)
        
        for style in sorted(styles):
            response += f"• **{style}**\n"
        
        response += "\nAll lashes are:\n"
        response += "✓ Applied individually for custom look\n"
        response += "✓ Lightweight and comfortable\n"
        response += "✓ Safe for your natural lashes\n"
        response += "✓ Long-lasting with proper care\n\n"
        response += "Would you like to know about pricing or book an appointment?"
        return response
    
    # Lash lift
    if 'lash lift' in message_lower:
        lash_services = CONFIG['services'].get('lash_services', {})
        lift_price = lash_services.get('Lash Lift', 'Contact us')
        tint_combo_price = lash_services.get('Lash Lift & Tint', 'Contact us')
        
        return f"""🌟 **Lash Lift Service:**

A lash lift curls and lifts your natural lashes for a beautiful, low-maintenance look!

✓ Lasts 6-8 weeks
✓ No extensions needed
✓ Wake up with curled lashes
✓ Can be paired with tinting

Pricing:
• Lash Lift: {format_price(lift_price)}
• Lash Lift & Tint: {format_price(tint_combo_price)}

Ready to book? {business_info['booking_url']}"""
    
    # Aftercare
    if any(word in message_lower for word in ['aftercare', 'care for', 'maintain', 'clean', 'how to care']):
        care_instructions = CONFIG.get('lash_care_instructions', {})
        
        response = "💧 **Lash Extension Aftercare:**\n\n"
        
        if 'after_appointment' in care_instructions:
            response += "**Immediately After:**\n"
            for instruction in care_instructions['after_appointment']:
                response += f"• {instruction}\n"
            response += "\n"
        
        if 'daily_care' in care_instructions:
            response += "**Daily Care:**\n"
            for instruction in care_instructions['daily_care']:
                response += f"• {instruction}\n"
            response += "\n"
        
        if 'avoid' in care_instructions:
            response += "**Avoid:**\n"
            for item in care_instructions['avoid']:
                response += f"✗ {item}\n"
            response += "\n"
        
        response += "Taking good care of your lashes helps them last longer! Any other questions?"
        return response
    
    # Brow services
    if any(word in message_lower for word in ['brow', 'eyebrow']):
        brow_services = CONFIG['services'].get('brow_services', {})
        if brow_services:
            response = "**Brow Services:**\n\n"
            for service, price in brow_services.items():
                response += f"• **{service}** - {format_price(price)}\n"
            response += "\nWhat brow service interests you?"
            return response
    
    # Check FAQ
    faq = CONFIG.get('faq', {})
    for question, answer in faq.items():
        # Check if any significant word from the question appears in the user message
        question_words = [w.lower() for w in question.split() if len(w) > 3]
        if any(word in message_lower for word in question_words):
            return f"**{question}**\n\n{answer}\n\nDo you have any other questions?"
    
    # Services overview
    if any(word in message_lower for word in ['service', 'offer', 'do you have', 'what do you do', 'what services']):
        services = CONFIG.get('services', {})
        service_categories = []
        
        if 'lash_extensions' in services:
            service_categories.append("Lash Extensions")
        if 'lash_services' in services:
            service_categories.append("Lash Lifts & Tints")
        if 'brow_services' in services:
            service_categories.append("Brow Services")
        if 'facial_services' in services:
            service_categories.append("Facial & Skincare")
        
        return f"We offer a variety of beauty services including:\n\n{', '.join(service_categories)}\n\nWould you like to know more about any specific service or see pricing?"
    
    # First time client
    if any(phrase in message_lower for phrase in ['first time', 'never had', 'new client', 'new customer']):
        first_time = CONFIG['policies'].get('first_time_clients', {})
        response = "Welcome! We're excited to have you! 🎉\n\n"
        
        if first_time.get('consultation_included'):
            response += "✓ Free consultation included\n"
        if first_time.get('patch_test_recommended'):
            response += "✓ We recommend a patch test if you have sensitive skin\n"
        if first_time.get('extra_time_needed'):
            response += "✓ Please allow a bit of extra time for your first visit\n"
        
        response += f"\nReady to book? {business_info['booking_url']}\n"
        response += f"Or call us at {business_info['phone']} with any questions!"
        return response
    
    # Thanks
    if any(word in message_lower for word in ['thank', 'thanks', 'appreciate']):
        return f"You're very welcome! If you have any other questions, feel free to ask. Otherwise, we look forward to seeing you soon! 💕\n\nBook online: {business_info['booking_url']}"
    
    # Default response
    return f"""I'd be happy to help you! I can provide information about:

📋 Services & Pricing
📅 Booking & Appointments  
📍 Location & Hours
💳 Deposit & Payment Policies
❓ Frequently Asked Questions
💆 Lash Care & Aftercare

You can also:
📞 Call us: {business_info['phone']}
🔗 Book online: {business_info['booking_url']}

What would you like to know?"""

def main():
    """Main application function"""
    business_info = CONFIG['business_info']
    
    st.set_page_config(
        page_title=f"{business_info['name']} - Chat Assistant",
        page_icon="✨",
        layout="wide"
    )
    
    # Custom CSS
    st.markdown("""
        <style>
        .main {
            background-color: #FFF5F7;
        }
        .stTextInput > div > div > input {
            background-color: white;
        }
        .chat-message {
            padding: 1rem;
            border-radius: 0.5rem;
            margin-bottom: 1rem;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Sidebar with business info
    with st.sidebar:
        # Logo - replace with actual logo
        logo_path = "logo.png"
        if os.path.exists(logo_path):
            st.image(logo_path, use_container_width=True)
        else:
            st.image("https://via.placeholder.com/300x100/FFB6C1/FFFFFF?text=Sunrae's+Beauty", use_container_width=True)
        
        st.title("💅 " + business_info['name'])
        st.markdown("---")
        st.markdown(f"📞 **{business_info['phone']}**")
        st.markdown(f"📍 **{business_info['location']}**")
        st.markdown(f"🌐 [{business_info['website']}]({business_info['booking_url']})")
        
        if 'instagram' in business_info:
            st.markdown(f"📱 **{business_info['instagram']}**")
        
        st.markdown("---")
        st.markdown("### Quick Links")
        if st.button("📅 Book Appointment", use_container_width=True):
            st.markdown(f"[Click here to book]({business_info['booking_url']})")
        
        st.markdown("---")
        st.markdown("### Services We Offer")
        services = CONFIG.get('services', {})
        if 'lash_extensions' in services:
            st.markdown("• Lash Extensions")
        if 'lash_services' in services:
            st.markdown("• Lash Lifts & Tints")
        if 'brow_services' in services:
            st.markdown("• Brow Services")
        if 'facial_services' in services:
            st.markdown("• Facials & Skincare")
    
    # Main chat area
    st.title("💬 Chat with Us!")
    st.markdown("Ask me anything about our services, pricing, booking, or policies!")
    
    # Initialize session state
    initialize_session_state()
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Type your message here..."):
        # Add user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Generate and display assistant response
        response = get_response(prompt)
        st.session_state.messages.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"):
            st.markdown(response)
    
    # Footer
    st.markdown("---")
    st.markdown(
        f"<div style='text-align: center; color: gray;'>© 2025 {business_info['name']} | "
        f"<a href='{business_info['booking_url']}'>Book Now</a></div>",
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
