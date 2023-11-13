from gforms import config


def extract_user_data(data) -> str | None:
    try:
        prompt = f"""
User's Personal Details:
Full Name: {data['Full Name']}
Email Address: {data['Email Address']}
Address: {data['Address (City, State)']}
Age: {data['Age']}
Gender: {data['Gender']}
Occupation: {data['Occupation (Your job position / University + field of study)']}

User's Daily Routine:
Usual wake up time on week days: {data['What time do you usually wake up on week days?']}
Morning Routine: {data['Describe your morning routine before starting your day (e.g., exercise, meditation, breakfast):']}
Usual start time for primary activity/activities: {data['What time do you usually start your primary activity / activities (work, classes, etc.)?']}
Usual end time for primary activities: {data['What time do you usually finish your primary activity / activities?']}
Monday start & end time: {data['Start and end time on Monday (e.g. Classes: 9:00AM - 2:00PM; Work: 3:00PM - 8:00PM)']}
Tuesday start & end time: {data['Start and end time on Tuesday']}
Wednesday start & end time: {data['Start and end time on Wednesday']}
Thursday start & end time: {data['Start and end time on Thursday']}
Friday start & end time: {data['Start and end time on Friday']}
Saturday start & end time: {data['Start and end time on Saturday']}
Sunday start & end time: {data['Start and end time on Sunday']}
Breaks: {data['Describe any breaks, activities, habits or routines you engage in during your primary activity (e.g., lunch breaks, study breaks):']}
Evening Routine: {data['Describe your evening routine or activities after finishing your primary activity / activities (e.g., gym, hobbies, dinner):']}
Sleep Routine: {data['Describe your sleep routine (e.g., reading, shower):']}
Bedtime: {data['What time do you usually go to bed?']}
Describe what is different about your weekends compared to your week days: {data['Describe what is different about your weekends compared to your week days?']}

# User's Goals and Aspirations
Areas of Improvement: {', '.join(data['Which areas are you looking to improve in?'])}
Top 3 Goals: {data['What are your top 3 personal development goals or goals in general for the next year?']}
Preferred Mentors: {data['Which mentors on our platform resonate most with you and why?(e.g., Elon Musk, Andrew Huberman, David Goggins, Joe Rogan, Alex Hormozi, Jordan Peterson, Other)']}
Preferred Learning Medium: {', '.join(data['Do you have a preference for books, podcasts, videos, or articles for learning?'])}
Habits or activities you struggle with: {data['What Habits or activities do you struggle with?']}
New good Habits you want to incorporate into your life: {data['What new good Habits do you want to incorporate into your life?']}
Additional properties to create your Blueprint?: {data["Is there anything else you'd like us to know or consider when creating your Blueprint?"]}
"""

        return prompt
    except Exception as x:
        config.logger.exception(x)
        return None
