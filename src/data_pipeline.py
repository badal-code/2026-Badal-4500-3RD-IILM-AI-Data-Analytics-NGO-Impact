from data_cleaning import clean_donations, clean_beneficiaries, clean_volunteers
from analytics import donation_summary, beneficiary_summary, volunteer_summary

def build_summary():
    donations = clean_donations()
    beneficiaries = clean_beneficiaries()
    volunteers = clean_volunteers()
    return {
        "donations": donation_summary(donations),
        "beneficiaries": beneficiary_summary(beneficiaries),
        "volunteers": volunteer_summary(volunteers)
    }

if __name__ == "__main__":
    print(build_summary())
