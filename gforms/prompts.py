from gforms import config


def extract_day_information(day: str, day_data: str) -> str:
    return f"""
    Create detailed schedule plan for - {day}. According to previously provided context. Details: {day_data}
    """


def extract_user_context(data) -> dict[str, str] | None:
    try:
        context = f"""
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
        monday_data = extract_day_information(
            "Monday",
            f"Monday start & end time: {data['Start and end time on Monday (e.g. Classes: 9:00AM - 2:00PM; Work: 3:00PM - 8:00PM)']}")
        tuesday_data = extract_day_information(
            "Tuesday",
            f"Tuesday start & end time: {data['Start and end time on Tuesday']}"
        )
        wednesday_data = extract_day_information(
            "Wednesday",
            f"Wednesday start & end time: {data['Start and end time on Wednesday']}"
        )
        thursday_data = extract_day_information(
            "Thursday",
            f"Thursday start & end time: {data['Start and end time on Thursday']}"
        )
        friday_data = extract_day_information(
            "Friday",
            f"Friday start & end time: {data['Start and end time on Friday']}"
        )
        saturday_data = extract_day_information(
            "Saturday",
            f"Saturday start & end time: {data['Start and end time on Saturday']}"
        )
        sunday_data = extract_day_information(
            "Sunday",
            f"Sunday start & end time: {data['Start and end time on Sunday']}"
        )

        return {
            "context": context,
            "monday": monday_data,
            "tuesday": tuesday_data,
            "wednesday": wednesday_data,
            "thursday": thursday_data,
            "friday": friday_data,
            "saturday": saturday_data,
            "sunday": sunday_data
        }
    except Exception as x:
        config.logger.exception(x)
        return None
