# Data Dictionary

## donations.csv
| Column | Meaning |
|---|---|
| donation_id | Unique donation identifier |
| donation_date | Date of donation |
| donor_type | Donor classification |
| state | Donor/record state |
| program | Supported NGO program |
| channel | Donation channel |
| amount_inr | Donation amount in INR |
| repeat_donor | Whether donor is represented as a repeat donor |

## beneficiaries.csv
| Column | Meaning |
|---|---|
| beneficiary_id | Unique beneficiary identifier |
| state | State |
| location_type | Urban or Rural |
| program | Program participation |
| age | Age |
| attendance_rate | Participation/attendance percentage |
| outcome_score | Synthetic impact score |
| engagement_level | Low, Medium or High engagement |

## volunteers.csv
| Column | Meaning |
|---|---|
| volunteer_id | Unique volunteer identifier |
| state | State |
| program | Program assignment |
| skill_area | Main contribution area |
| hours_contributed | Volunteer hours |
| months_active | Months active |

## programs.csv
| Column | Meaning |
|---|---|
| program | Program name |
| annual_budget_inr | Demonstration annual budget |
| planned_beneficiaries | Planned beneficiary count |
| actual_beneficiaries | Count represented in synthetic beneficiary data |
| cost_per_beneficiary_inr | Budget divided by represented beneficiaries |
