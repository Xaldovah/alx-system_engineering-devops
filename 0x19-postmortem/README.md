# Postmortem: The Day the Database Took a Nap
## Issue Summary:
•	Duration: Siesta started on 8th of November at 10:00 AM and concluded fashionably late at 1:30 PM (UTC).
•	Impact: Our web service decided to channel its inner sloth, leading to a 30% drop in response time. Approximately 15% of users got an unexpected break with slow loading times and sporadic disconnections.
## Timeline:
•	Issue Detection: The alarm clock rang at 10:00 AM, courtesy of our vigilant monitoring system throwing a fit about skyrocketing response time.
•	Detection Method: The monitoring system slid into our DMs with alerts, screaming, "Nairobi, we have a problem!"
•	Actions Taken:
•	Investigation: The crack detective team (a.k.a. the engineering squad) started digging, suspecting foul play in the web server and database realms.
•	Assumptions: Initially, the blame game pointed fingers at the database, accusing it of sleeping on the job.
•	Misleading Paths:
•	Like a wild goose chase, the team chased down the path of database query optimization issues.
•	Network latency got some unwarranted attention, playing the innocent bystander with no connection to the crime.
•	Escalation:
•	The incident report went up the corporate ladder to the DevOps and Database teams, who promptly put on their Sherlock hats.
•	Resolution:
•	Unmasking the villain, we discovered a misconfigured database connection pool, caught napping and causing delays in the query execution.
•	The database connection pool received a stern talking-to, a fresh cup of coffee, and a makeover.
## Root Cause and Resolution:
•	Root Cause:
•	The database connection pool decided to snooze on the job due to a misconfiguration, leading to performance hiccups.
•	Resolution:
•	The configuration got a facelift, with a spa day for the connection pool—max connections were adjusted, and its efficiency got a makeover.
•	Database queries attended therapy sessions and came out optimized and rejuvenated.
## Corrective and Preventative Measures:
### Improvements:
    •	Introduced a snazzy new monitoring system with a dash of pizzazz to detect potential database drama.
    •	Automated testing for the database connection pool, turning it into a responsible adult.
    •	Scheduled regular performance audits, the equivalent of a health check for our systems.
### Tasks:
    • TODO: Patch Nginx Server: Giving Nginx a fresh coat of paint, ensuring it stays in style.
    •	TODO: Add Memory Monitoring: Implemented a memory lifeguard to prevent any potential drowning incidents.

*In a world of tech jargon and debugging blues, our web service decided to take a leisurely stroll through the realm of performance issues. Join us as we uncover the misadventures of a misconfigured database connection pool, the unsung hero in this tale. Will it emerge from its slumber, or will the web service continue its quest for the perfect nap? Buckle up for a rollercoaster of emotions, drama, and a touch of tech therapy.*
