# Call Type to Category Type Mapping

**Last Updated:** 2026-01-09

This document provides a comprehensive breakdown of Call Types (Incident Types) organized by Category Type, based on the ESRI standardized classification system.

## Overview

- **Total Call Types:** 649
- **Total Categories:** 11 (ESRI Standard Categories Only)
- **Source File:** `CallType_Categories.csv` (Single Source of Truth)
- **File Format:** Incident, Incident_Norm, Category_Type, Response_Type
- **Location:** `09_Reference/Classifications/CallTypes/CallType_Categories.csv`

**Important:** All entries use only the 11 ESRI standard categories. Non-standard categories (Miscellaneous, Uncategorized, Criminal Investigation, Patrol and Prevention, Community Engagement and Services) have been mapped to the appropriate ESRI standard categories.

## Important Notes

- **Incident_Norm Column**: The reference file includes an `Incident_Norm` column for normalized incident type matching, enabling better fuzzy matching and handling of variations
- **E.D.P. Variations**: All E.D.P. variations (E.D.P., EDP, edp, e.d.p., E.D.P, E D P, E D.P., EDP.) map to "Mental Health Incident"
  - Category: "Public Safety and Welfare"
  - Response: "Emergency"
  - Incident_Norm: "Mental Health Incident"

## Category Breakdown

### Administrative and Support

- **Total Call Types:** 122
- **Response Types:** Routine (122)

**Call Types in this category:**

- A.C.O.R.N. Test
- ABC Liquor License Applicant
- Academy Assignment
- Active/Administratively Closed
- Administrative Assignment
- Applicant ABC License
- Applicant ABC License (Server)
- Applicant ABC Liquor License (Business)
- Applicant AD Material License
- Applicant All Others
- Applicant City Employee
- Applicant Concealed Carry
- Applicant Firearm(s)
- Applicant Handicapped Permit
- Applicant Ice Cream Vendor
- Applicant Jewelry
- Applicant Landscaper
- Applicant Limo
- Applicant Peddling License
- Applicant Pistol Permit
- Applicant Police Auxiliary
- Applicant Police Officer
- Applicant Snow Removal
- Applicant Solicitor
- Applicant Spa Therapy
- Applicant Taxi
- Applicant Towing
- Applicant Vending License
- Background Checks
- CCH / III Request
- Canceled Call
- Canvassing / Peddling Permit
- Car Wash
- Civil Defense Test
- Coffee Break
- Computer Issue - Desktop
- Computer Issue - Vehicle
- Conditional Dismissal Process
- Court - Federal
- Court - Municipal
- Court - Municipal Prisoner
- Court - Other Municipality
- Court - Superior
- Court Officer
- Court Order
- Desk Coverage
- Docket – Drop Off
- Docket – Pick up
- Exceptionally Cleared/Closed
- Expungement
- FTO Documentation
- Fingerprints
- General Information
- Generated in Error
- Generator Test
- Good Conduct Letter Request
- Group
- HQ Assignment
- ICE Notification
- Improper Records
- Information
- Meal Break
- Meeting
- NCIC Record
- No Investigation
- Notification Request
- OPRA Request
- Off the Air
- Parole/Probation Registry
- Peace Officer
- Photography
- Prisoner Log
- Prisoner Transport
- Property Damage - Police Vehicle
- Property Disposition
- Property Returned - Court Ordered
- Property Returned - Lost and Found
- Radio Coverage
- Records Request
- Records Request - DCPP (DYFS)
- Refuel Vehicle
- Relief / Personal
- Road Job/Outside Assignment
- Service - Subpoena
- Service - Summons
- Sex Offender - General
- Sex Offender - Serve Documents
- Sex Offender - Serve Tier Papers
- Sex Offender - Travel
- Sex Offender Registration
- Sex Offender Registration - Employment
- Sex Offender Registration - School Enrollment
- Sex Offender-Removal Order
- Sex Offender-Serve Tier Papers
- Special Assignment
- Surrender of Ammunition
- Surrender of Weapon
- Surrendered Firearm ID Card
- Surrendered License Plates
- Task Assignment
- Time Check
- Training
- Training Record
- Transportation
- U-Visa
- Unfounded Incident
- Unfounded/Closed
- Vacation
- Validation
- Vehicle Maintenance
- Warning Issued
- Warrant Recall

### Assistance and Mutual Aid

- **Total Call Types:** 21
- **Response Types:** Routine (15), Urgent (6)

**Call Types in this category:**

- Assist Motorist
- Assist Other Agency
- Assist Own Agency (Backup)
- Cooperative Arrest - Little Ferry
- Cooperative Arrest - Maywood
- Cooperative Arrest - Ridgefield Park
- Cooperative Arrest - So. Hackensack
- Courtesy Transport
- D.P.W. Assist
- Escort - Money
- Fire Department Call
- Funeral Escort
- Lock-Out Residence
- Motor Vehicle Lock-out
- Mutual Aid - E.M.S.
- Mutual Aid - Fire
- Mutual Aid - Police
- Non-Emergency Assist
- Parks Department Needed
- Police Assist
- Stranded Party

### Community Engagement

- **Total Call Types:** 20
- **Response Types:** Routine (20)

**Call Types in this category:**

- Car Seat Installation
- Church Crossing
- Community Engagement - Community Policing
- Community Engagement - Crime Prevention
- Community Engagement - Crisis Intervention
- Community Engagement - Emergency Response
- Community Engagement - Online Engagement
- Community Engagement - Public Education
- Community Engagement - School Outreach
- Community Engagement - Traffic Safety
- Community Engagement - Victim Support
- DARE Assignment
- Presentation Community Policing
- School Crossing
- School Detail

### Criminal Incidents

- **Total Call Types:** 201
- **Response Types:** Routine (115), Emergency (31), Urgent (55)

**Call Types in this category:**

- Aggravated Assault - 2C:12-1b
- Aggravated Sexual Assault - 2C:14-2a
- Aiding Suicide - 2C:11-6
- Alcohol/School Property - 2C:33-16
- Annoying Phone Calls - 2C:33-4a
- Arrest Process
- Arrest and JV Complaints
- Arson - 2C:17-1
- Attempted Burglary - 2C:18-2
- Attempted Burglary - Commercial - 2C:18-2
- Attempted Burglary - Residence - 2C:18-2
- Bad Checks - 2C:21-5
- Bias Incident
- Bribery - 2C:27-2
- Burglar Tools - 2C:5-5
- Burglary - Auto - 2C:18-2
- Burglary - Commercial - 2C:18-2
- Burglary - Residence - 2C:18-2
- CDS/Dist.; School Property - 2C:35-7
- CDS/Distribution - 2C:35-5
- CDS/Possession: Influence - 2C:35-10
- CDS: Obtain by Fraud - 2C:35-13
- Carjacking - 2C:15-2
- Catalytic Converter Theft
- Cleared - Arrest
- Cleared-Arrest
- Compensation - 2C:27-4
- Compensation/Public Servant - 2C:27-7
- Complaint Signed
- Compounding - 2C:29-4
- Conspiracy - 2C:5-2
- Contempt of Court - 2C:29-9
- Counterfeit Money
- Creating a Hazard - 2C:40-1
- Credit Cards - Unlawful Use - 2C:21-6
- Credit Practices - 2C:21-19
- Criminal Attempt - 2C:5-1
- Criminal Coercion - 2C:13-5
- Criminal Homicide - 2C:11-2
- Criminal Mischief - 2C:17-3
- Criminal Mischief - Graffiti - 2C:17-3
- Criminal Mischief - Park - 2C:17-3
- Criminal Mischief - School - 2C:17-3
- Criminal Mischief - Vehicle - 2C:17-3
- Criminal Restraint - 2C:13-2
- Criminal Sexual Contact - 2C:14-3a
- Criminal Simulation - 2C:21-2
- Criminal Trespass - 2C:18-3
- Cyber Harassment - 2C:33-4.1
- Damage to Property: Threats - 2C:33-11
- Deceased Person/Sexual Pen. - 2C:34-5
- Desecration/Venerated Obj. - 2C:33-9
- Disorderly Conduct - 2C:33-2
- Disrupting Meet/Procession - 2C:33-8s
- Domestic Violence - 2C:25-21
- Drug Paraphernalia - 2C:36-2
- Embezzlement
- Endangering Welfare - 2C:24-4
- Endangering Welfare - 2C:24-7
- Endangering Welfare - 2C:24-8
- Escape - 2C:29-5
- Evidence Tampering - 2C:28-6
- False Imprisonment - 2C:13-3
- False Public Alarm - 2C:33-3
- False Reports - 2C:28-4
- False Swearing - 2C:28-2
- Fear of Bodily Violence - 2C:33-10
- Fencing - 2C:20-7.1
- Food/Drug Tampering - 2C:40-17
- Forgery - 2C:21-1
- Fraud
- Fugitive from Justice
- Gifts/Public Servant - 2C:27-6
- Harassment - 2C:33-4
- Hindering Apprehension - 2C:29-3
- Homicide - 2C:11-2
- Hypodermic/Possession - 2C:36-6
- Identity Theft
- Imitation CDS - 2C:35-11
- Impersonating Public Servant - 2C:28-9
- Implements for Escape - 2C:29-6
- Injury/Law Enforce. Animals - 2C:29-3.1
- Interception/Emerg. Comm. - 2C:33-21
- Interference - 2C:29-1
- Interference With Custody - 2C:13-4
- Interference w/Transport. - 2C:33-14
- Interference/Railway Signals - 2C:33-14.1
- Invasion of Privacy - Observing
- Kidnapping - 2C:13-1
- Lewdness - 2C:14-4
- Loitering/CDS Offense - 2C:33-2.1
- M.V. Master Keys - 2C:5-6
- Maintaining a Nuisance - 2C:33-12
- Manslaughter - 2C:11-4
- Megan's Law Violation
- Money Laundering
- Motor Vehicle Theft - 2C:20-3
- Murder - 2C:11-3
- Non-Support - 2C:24-5
- Obscenity - Over 18 yrs. - 2C:34-2
- Obscenity - Under 18 yrs. - 2C:34-3
- Obscenity Public Comm. - 2C:34-4
- Obscenity Retail Display - 2C:34-3.2
- Obstructing Highways/Pass. - 2C:33-7
- Obstruction of Govermental Function
- Obstruction of Governmental Function
- Official Misconduct - 2C:30-2
- Paging Device/Illicit Use - 2C:33-20
- Paging Device/Minors - 2C:33-18
- Paging Device/Student - 2C:33-19
- Perjury 2C:28-1
- Prohibited Weapons - 2C:39-3
- Prostitution - 2C:34-1
- Public Safety/Sr. Citizens - 2C:24-8
- Receiving Stolen Property - 2C:20-7
- Reckless Endangerment - 2C:12-2
- Resisting Arrest/Eluding - 2C:29-2
- Retaliation/Official Action - 2C:27-5
- Riot - Failure to Disperse - 2C:33-1
- Robbery - 2C:15-1
- Service - FRO
- Service - TRO
- Sexual Assault - 2C:14-2b
- Shoplifting - 2C:20-11
- Simple Assault - 2C:12-1a
- Slugs - 2C:21-18
- Stalking - 2C:12-10
- Stolen Article
- Summons
- Tampering: Public Records - 2C:28-7
- Terroristic Threats - 2C:12-3
- Theft - 2C:20-3
- Theft by Deception - 2C:20-4
- Theft by Extortion - 2C:20-5
- Theft of Identity - 2C:21-17
- Theft of Lost/Mislaid Property - 2C:20-6
- Theft of Services - 2C:20-8
- Theft/Disposition - 2C:20-9
- Unauthorized Intercept./Comm. - 2C:33-22
- Unlawful Possess./Weapons - 2C:39-5
- Unlawful Taking - 2C:20-10
- Unlawful Use Of 9-1-1 Sys. - 2C:33-3e
- Unsworn Falsification - 2C:28-3
- Vehicular Homicide - 2C:11-5
- Violation FRO - 2C:29-9b
- Violation TRO - 2C:29-9b
- Violation of Court Order
- Violation: TRO/ FRO - 2C:29-9b
- Wagering/Official Action - 2C:30-3
- Warrant Arrest
- Weapons - Unlawful Purposes - 2C:39-4
- Weapons Seizure - 2C:25-21d
- Widespread Damage - 2C:17-2
- Witness Tampering - 2C:28-5
- Wrongful Impersonating - 2C:21-1

### Emergency Response

- **Total Call Types:** 33
- **Response Types:** Emergency (32), Urgent (1)

**Call Types in this category:**

- 9-1-1 Call
- Abandoned 9-1-1 Emergency
- Alarm - Burglar
- Alarm - Fire
- Alarm - Panic
- Aviation Accident
- Bomb Scare
- D.O.A
- Disarm a Law Enforcement Officer
- Disarm a Law Enforcement Officer - Attempt
- Emergency Access Card Use
- Fight - Armed
- Fight - Unarmed
- Fire
- HAZ-MAT Incident
- Handle With Care - Notification
- Hostage Situation
- Service - FERPO
- Service - TERPO
- Shooting
- Shots Fired Investigation
- Stabbing
- Sudden Death Investigation
- Suicide
- Unintentional Discharge

### Investigations and Follow-Ups

- **Total Call Types:** 44
- **Response Types:** Routine (33), Urgent (11)

**Call Types in this category:**

- ALPR Analysis
- ALPR Flag
- BOLO
- DNA Sample
- Detective Bureau Detail
- Discovery - Criminal
- Discovery - Motor Vehicle
- Discovery - Non Specific
- Evidence Delivery
- Evidence Retrieval
- Facial Recognition Request
- Field Contact/ Information
- General Investigation
- Investigation - Follow-Up
- Investigation Follow-Up
- Lo-Jack Hit - Tracking Signal
- Missing Person - Adult
- Missing Person - Return - Adult
- Narcotics Investigation
- Pawned Item(s)
- Property - Found
- Property - Lost
- Property Recovered - Stolen
- Recovered Stolen - Article
- Recovered Stolen - Firearm
- Recovered Stolen License Plate
- Recovered Stolen Vehicle
- Search Warrant Execution - CDW
- Search Warrant Execution - Structure
- Search Warrant Execution - Vehicle
- Search Warrant Execution- Structure
- Sex Offender - Address Verification
- Sex Offender - Intent to Move
- Sex Offender Investigation
- Suspicious Activity Report
- Suspicious Activity Submission
- Suspicious Incident
- Suspicious Item
- Suspicious Person
- Suspicious Vehicle
- TAS Alert - Stolen License Plate
- Unknown Investigation

### Juvenile-Related Incidents

- **Total Call Types:** 16
- **Response Types:** Routine (10), Urgent (4), Emergency (2)

**Call Types in this category:**

- CDS/Employing Juvenile - 2C:35-6
- Child Abuse - Title 9
- Compulsory School Attend. - Title 18A:38-2
- DCPP (DYFS)
- Enticing a Child - 2C:13-6
- Juvenile Complaint (Criminal)
- Juvenile Complaint (Non-Criminal)
- Juvenile Complaint Signed
- Juvenile Investigation
- Missing Person - Juvenile
- Missing Person - Return - Juvenile
- NARCAN Deployment - Juvenile - Aid
- Overdose - Juvenile - Aid
- Stationhouse Adjustment
- TOT DCP&P
- Truancy

### Public Safety and Welfare

- **Total Call Types:** 85
- **Response Types:** Routine (52), Urgent (22), Emergency (11)

**Call Types in this category:**

- Alarm - Other
- Animal Bite Incident
- Boating Incident
- Child Custody Dispute
- Code Blue
- Constable - Secured Park Facilities
- Dead Animal
- Dispute
- Disturbance
- Duty to Warn - Notification
- Hazard All Other
- Hazardous Condition - Health / Welfare
- Hazardous Condition - Sewer Call
- Injured On Duty
- Insecure Building
- Intoxicated Person
- Landlord / Tenant Dispute
- Medical Call
- Medical Call - Oxygen
- Medical Call/Injury
- Mental Health Incident
- Municipal Property/Building Check
- NARCAN Deployment - Adult - Aid
- Overdose - Adult - Aid
- Patrol Check
- Patrol Check - Extra Duty Detail
- Property Damage - City Property
- Property Damage - Non-Criminal
- Shopping Cart
- Street Light
- Structure Damage
- Suicidal Party
- TAPS - Business
- TAPS - Housing
- TAPS - Medical Facility
- TAPS - Other
- TAPS - Park
- TAPS - Parking Garage
- TAPS - Religious Facility
- TAPS - School
- Tree limb down
- Unwanted Person
- Utility Incident
- Vacant House
- Virtual - Patrol
- Weather Alerts
- Welfare Check
- Wire Down

### Regulatory and Ordinance

- **Total Call Types:** 31
- **Response Types:** Routine (30), Urgent (1)

**Call Types in this category:**

- ABC Advisory Check
- ABC Inspection
- ABC Violation
- Alarm Ordinance
- Alcoholic Beverage - Hours of Sale
- Alcoholic Beverage - New Years Day Hours of Sale
- Alcoholic Beverage - Serving Underage
- Alcoholic Beverage - Sunday Hours of Sale
- Alcoholic Beverage - Unlicensed Bartender
- Animal Complaint
- Animal Cruelty
- Canvassing without Permit
- City Ordinance
- City Ordinance Warning
- Construction Hours
- Dogs Defecating
- Dogs at Large
- Drinking in Public
- Fireworks Complaint
- Fish and Game Violation Title 23
- Illegal Dumping
- Noise Complaint
- Sale of Cigarettes to Minors - 2A:170-51
- Serving Alcohol to Minors - 2C:33-17
- Smoking Prohibited
- Snow Plowed onto Public Street
- Snow Removal
- Urinating in Public
- Vending Without Permit

### Special Operations and Tactical

- **Total Call Types:** 19
- **Response Types:** Routine (10), Emergency (6), Urgent (3)

**Call Types in this category:**

- A.T.R.A.
- Controlled Buy
- Controlled CDS Purchase
- ESU - Response
- ESU - Training
- PRD Activation
- Pursuit - Foot
- Pursuit - Motor Vehicle
- RDF Deployment
- RDT Deployment
- TAPS - ESU - Business
- TAPS - ESU - Medical Facility
- TAPS - ESU - Park
- TAPS - ESU - Parking Garage
- TAPS - ESU - Religious Facility
- TAPS - ESU - School
- UAS Operation
- Undercover Buy

### Traffic and Motor Vehicle

- **Total Call Types:** 57
- **Response Types:** Routine (39), Urgent (12), Emergency (6)

**Call Types in this category:**

- Abandoned Auto
- Blocked Driveway
- Breath Test - Refusal - 39:4-50.2
- Checked Road Conditions (Weather)
- Disabled Motor Vehicle
- Driving While Intoxicated - 39:4-50
- Hazard - Pothole
- Hazardous Road Condition - Flooding
- Hazardous Road Condition - General
- Hazardous Road Condition - Ice
- Leaving Scene of an Acc. - 39:4-129
- License Plate-Lost/Stolen
- Motor Vehicle - Private Property Tow
- Motor Vehicle Complaint
- Motor Vehicle Crash
- Motor Vehicle Crash -  W/Injury
- Motor Vehicle Crash -  w/injury
- Motor Vehicle Crash - Bicyclist Struck
- Motor Vehicle Crash - Hit and Run
- Motor Vehicle Crash - Pedestrian Struck
- Motor Vehicle Crash - Police Vehicle
- Motor Vehicle Crash - w/injury
- Motor Vehicle Impound
- Motor Vehicle Stop
- Motor Vehicle Violation
- Motor Vehicle Violation - Commercial Vehicle
- Motor Vehicle Violation - Private Property
- Overnight Parking
- Parking Complaint
- Parking Offense
- Poss. CDS in MV - 39:4-49.1
- Radar Detail
- Radar Trailer Deployed
- Repossessed Motor Vehicle
- Suspended Drivers License - 39:3-40
- Suspended Registration - 39:3-40
- Temporary Parking
- Traffic Bureau Report
- Traffic Detail
- Traffic Detail - Road Closure
- Traffic Enforcement Detail
- Traffic Hazard
- Traffic Light Malfunction
- Traffic Sign / Signal Malfunction
- Uninsured Vehicle - 39:6b-2
- Unregistered Vehicle - 39:3-4

