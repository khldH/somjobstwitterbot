from datetime import datetime


def get_new_jobs_posted_today(db_con):
    table = db_con.Table("jobs")
    jobs = table.scan()["Items"]
    jobs_posted_today = []
    for job in jobs:
        if job["source"] == "Somali jobs":
            job["days_since_posted"] = (
                datetime.now().date()
                - datetime.strptime(job["posted_date"], "%d %b %Y").date()
            ).days
        else:
            job["days_since_posted"] = (
                datetime.now().date()
                - datetime.fromisoformat(job["posted_date"]).date()
            ).days
        if job["days_since_posted"] == 0:
            jobs_posted_today.append(job)
    return jobs_posted_today


def tweet_jobs_posted_today(jobs, client):
    for job in jobs:
        job_title = job["title"]
        org = job["organization"]
        url = job["url"]

        status_update = "#NEW SOMALI JOB ALERT"
        status_update = (
            status_update
            + "\n"
            + job_title
            + "\n"
            + org
            + "\n"
            + url
            + "\n"
            + "#Somalijobs,#Somaliland, #Somalia"
        )
        try:
            client.create_tweet(text=status_update)
            print(status_update, "tweet sent successfully")
        except Exception as e:
            print(e)
