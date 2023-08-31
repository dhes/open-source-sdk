# This protocol started as a copy of the breast cancer screening protocol. 
# As of 2023-08-30 it is a first draft. 
# I have many questions about how this works. 
# This code is certainly not functional, has not been tested and should not be applied in productions. 

from typing import cast

import arrow

from canvas_workflow_kit import events
from canvas_workflow_kit.protocol import (
    CONTEXT_REPORT,
    STATUS_DUE,
    STATUS_SATISFIED,
    ClinicalQualityMeasure,
    ProtocolResult,
)
from canvas_workflow_kit.constants import CHANGE_TYPE

# @canvas-adr-0006
from canvas_workflow_kit.value_set.specials import AaaScreeningUltrasound # TO DO where do I set up specials?
# coding for AAA screening see 
# https://www.cms.gov/medicare-coverage-database/view/article.aspx?articleId=55071
# https://braccoreimbursement.com/bracco-reimbursement-faq/proper-coding-for-ultrasound-to-rule-out-or-follow-up-on-aaa-plus-other-cpt-codes-for-related-other-organ-and-duplex-studies-2/
# https://loinc.org/79374-5/
# I'm stuck here. I don't know where to create a special value set. Many of the values can be found in my repository *abdominal-aortic-aneurysm-screening*. 

# flake8: noqa
from canvas_workflow_kit.value_set.v2021 import (
    AnnualWellnessVisit,
    # BilateralMastectomy,
    HomeHealthcareServices,
    # Mammography,
    OfficeVisit,
    PreventiveCareServicesEstablishedOfficeVisit18AndUp,
    PreventiveCareServicesInitialOfficeVisit18AndUp,
    # StatusPostLeftMastectomy,
    # StatusPostRightMastectomy,
    # UnilateralMastectomy,
    AaaRepair, 
    FemoralAneurysmRepair
)
from canvas_workflow_kit.value_set.value_set import ValueSet


# class MammographyImaging(ValueSet):
#     VALUE_SET_NAME = "Mammography Imaging"
#     CPT = {"77067"}
class AortaImagingForScreening(ValueSet):
      VALUE_SET_NAME = "Aorta Ultrasound for AAA Screening "
      CPT = {"76706"}
      LOINC = {"79374-5"}


# EncounterForMammographCondition = {
# ...."code": "Z1231",
#     "system": "ICD-10",
#     "display": "Encounter for screening mammogram for malignant neoplasm of breast",
# }
EncounterForAaaScreening = {
    "code": "Z13.6", 
    "system": "ICD-10",
    "display": "encounter for screening for cardiovascular disorders"
}
# CMS also seems to want one of these:
# Z87.891, F17.210, F17.211, F17.213, F17.218 and F17.219 OR
# Z84.89 for family history of other specified conditions

# class BreastCancerScreening(ClinicalQualityMeasure):
#     """
#     Breast Cancer Screening

#     Description: Percentage of women 50-74 years of age who had a mammogram to screen for breast
#     cancer

#     Definition: None

#     Rationale: Breast cancer is one of the most common types of cancers, accounting for a quarter
#     of all new cancer diagnoses for women in the U.S. (BreastCancer.Org, 2011). It ranks as the
#     second leading cause of cancer-related mortality in women, accounting for nearly 40,000
#     estimated deaths in 2013 (American Cancer Society, 2011).

#     According to the National Cancer Institute's Surveillance Epidemiology and End Results program,
#     the chance of a woman being diagnosed with breast cancer in a given year increases with age. By
#     age 30, it is one in 2,212. By age 40, the chances increase to one in 235, by age 50, it
#     becomes one in 54, and, by age 60, it is one in 25. From 2004 to 2008, the median age at the
#     time of breast cancer diagnosis was 61 years among adult women (Tangka et al, 2010).

#     In the U.S., costs associated with a diagnosis of breast cancer range from $451 to $2,520,
#     factoring in continued testing, multiple office visits, and varying procedures. The total costs
#     related to breast cancer add up to nearly $7 billion per year in the U.S., including $2 billion
#     spent on late-stage treatment (Lavigne et al, 2008; Boykoff et al, 2009).

#     Guidance: Patient self-report for procedures as well as diagnostic studies should be recorded
#     in 'Procedure, Performed' template or 'Diagnostic Study, Performed' template in QRDA-1. Patient
#     self-report is not allowed for laboratory tests.

#     This measure evaluates primary screening. Do not count biopsies, breast ultrasounds, MRIs or
#     tomosynthesis (3D mammography), because they are not appropriate methods for primary breast
#     cancer screening.

#     More information: https://ecqi.healthit.gov/sites/default/files/ecqm/measures/CMS125v6.html
#     """

class AbdominalAortaAneurysmScreening(ClinicalQualityMeasure):
    """
    Abdominal Aortic Aneurysm: Screening
    
    Description: Percentage of men who are former or current smokers who had a US of the abdominal aorta for screening
    
    Definition: None
    
    Rationale: There is adequate evidence that ultrasonography is a safe and accurate screening test 
    for AA. There is adequate evidence that 1-time screening for AAA with ultrasonography results in 
    a moderate benefit in men aged 65 to 75 y who have ever smoked. here is adequate evidence that 
    the harms associated with 1-time screening for AAA with ultrasonography are small to moderate. 
    There is moderate certainty that screening for AAA with ultrasonography in men aged 65 to 75 y 
    who have ever smoked has a moderate net benefit. 
    
    More Information: https://www.uspreventiveservicestaskforce.org/uspstf/document/RecommendationStatementFinal/abdominal-aortic-aneurysm-screening#bootstrap-panel--11
    """

    # class Meta:
    #     title = "Breast Cancer Screening"
    #     version = "2023v1"  # is this my version or an official guideline version or an eCQI version or what?

    #     # 27 months, but we want to ensure it is displayed as 2 years, 3 months
    #     # 27 * 30 is 2 years, 2 months, and some amount of days
    #     default_display_interval_in_days = (365 * 2) + (3 * 30)

    #     description = (
    #         "Women 50-74 years of age who have not had a mammogram to screen for "
    #         "breast cancer within the last 27 months."
    #     )
    #     information = (
    #         "https://ecqi.healthit.gov/sites/default/files/ecqm/measures/CMS125v6.html"
    #     )

    #     identifiers = ["BreastCancerScreening"]

    #     types = ["CQM"]

    #     responds_to_event_types = [
    #         events.HEALTH_MAINTENANCE,
    #     ]

    #     authors = [
    #         "National Committee for Quality Assurance",
    #     ]

    #     references = [
    #         "American Cancer Society. 2010. Cancer Facts & Figures 2010. Atlanta: American Cancer Society.",
    #         'National Cancer Institute. 2010. "Breast Cancer Screening." http://www.cancer.gov/cancertopics/pdq/screening/breast/healthprofessional',
    #         "National Business Group on Health. 2011. Pathways to Managing Cancer in the Workplace. Washington: National Business Group on Health.",
    #         'U.S. Preventive Services Task Force (USPSTF). 2009. 1) "Screening for breast cancer: U.S. Preventive Services Task Force recommendation statement." 2) "December 2009 addendum." Ann Intern Med 151(10):716-726.',
    #         "BreastCancer.org. 2012. U.S. Breast Cancer Statistics. www.breastcancer.org/symptoms/understand_bc/statistics.jsp",
    #     ]

    #     compute_on_change_types = [
    #         CHANGE_TYPE.PROTOCOL_OVERRIDE,
    #         CHANGE_TYPE.CONDITION,
    #         CHANGE_TYPE.IMAGING_REPORT,
    #         CHANGE_TYPE.PATIENT,
    #     ]

    class Meta:
        title = "Abdominal Aortic Aneurysm Screening"
        version = "2023v1"  # is this my version or an official guideline version or an eCQI version or what? I didn't make any changes

        # 27 months, but we want to ensure it is displayed as 2 years, 3 months
        # 27 * 30 is 2 years, 2 months, and some amount of days
        default_display_interval_in_days = (365 * 2) + (3 * 30) # TO DO not sure what to do with this. Screening is one time so probably NA. 

        description = (
            "Men 65-75 years of age who ever smoked should have 1-time ultrasonography screening for "
            "abdominal aortic aneurysm (AAA). "
        )
        information = (
            "https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/abdominal-aortic-aneurysm-screening"
        )

        identifiers = ["AbdominalAortaAneurysmScreening"]

        types = ["CQM"]

        responds_to_event_types = [ # no change
            events.HEALTH_MAINTENANCE,
        ]

        authors = [
            "U.S. Preventive Services Task Force",
        ]

        references = [
            "Guirguis-Blake JM, Beil TL, Senger CA, Coppola EL. Primary Care Screening for Abdominal Aortic Aneurysm: Updated Systematic Review for the U.S. Preventive Services Task Force. Evidence Synthesis No. 184. AHRQ Publication No. 19-05253-EF-1. Rockville, MD: Agency for Healthcare Research and Quality; 2019.",
            "Guirguis-Blake JM, Beil TL, Senger CA, Coppola EL. Primary care screening for abdominal aortic aneurysm: evidence report and systematic review for the US Preventive Services Task Force. JAMA. 2019;322(22):2219-2238.",
            "Svensjö S, Björck M, Gürtelschmid M, Djavani Gidlund K, Hellberg A, Wanhainen A. Low prevalence of abdominal aortic aneurysm among 65-year-old Swedish men indicates a change in the epidemiology of the disease. Circulation. 2011;124(10):1118-23.",
        ]

        compute_on_change_types = [
            CHANGE_TYPE.PROTOCOL_OVERRIDE,
            CHANGE_TYPE.CONDITION,
            CHANGE_TYPE.IMAGING_REPORT,
            CHANGE_TYPE.PATIENT,
        ]

    _on_date = None
    AGE_RANGE_START = 65
    AGE_RANGE_END = 75
    # EXTRA_SCREENING_MONTHS = 15 # TO DO not sure what this means, suspect NA

    # def had_mastectomy(self) -> bool:
    #     if self.patient.conditions.find(BilateralMastectomy).starts_before(
    #         self.timeframe.end
    #     ):
    #         return True

    #     unilateral_mastectomy = self.patient.conditions.find(
    #         UnilateralMastectomy
    #     ).starts_before(self.timeframe.end)
    #     if 2 == len(unilateral_mastectomy):
    #         return True

    #     if unilateral_mastectomy and self.patient.conditions.find(
    #         StatusPostRightMastectomy
    #     ).starts_before(self.timeframe.end):
    #         return True

    #     if unilateral_mastectomy and self.patient.conditions.find(
    #         StatusPostLeftMastectomy
    #     ).starts_before(self.timeframe.end):
    #         return True

    #     return False
    
    def had_aaa_repair(self) -> bool:
        if self.patient.conditions.find(AaaRepair).starts_before(
            self.timeframe.end
        ):
            return True

        # unilateral_mastectomy = self.patient.conditions.find(
        #     UnilateralMastectomy
        # ).starts_before(self.timeframe.end)
        # if 2 == len(unilateral_mastectomy):
        #     return True

        # if unilateral_mastectomy and self.patient.conditions.find(
        #     StatusPostRightMastectomy
        # ).starts_before(self.timeframe.end):
        #     return True

        # if unilateral_mastectomy and self.patient.conditions.find(
        #     StatusPostLeftMastectomy
        # ).starts_before(self.timeframe.end):
        #     return True

        return False


    def first_due_in(self) -> int | None:
        if (
            self.patient.is_female
            and self.patient.age_at(self.timeframe.end) < self.AGE_RANGE_START
            and not self.had_mastectomy()
        ):
            return cast(
                int,
                (
                    self.patient.birthday.shift(years=self.AGE_RANGE_START)
                    - self.timeframe.end
                ).days,
            )
        return None

    def in_initial_population(self) -> bool: # TO DO this is a CQM thing. I'm doing clinical decision support. 
        """
        Initial population: Men 65-75 years of age who ever smoked 
        """
        return cast(
            bool,
            self.patient.age_at_between(
                self.timeframe.end, self.AGE_RANGE_START, self.AGE_RANGE_END
            )
            and self.patient.is_male
            # and (
            #     self.patient.has_visit_within(
            #         self.timeframe,
            #         (
            #             OfficeVisit
            #             | PreventiveCareServicesInitialOfficeVisit18AndUp
            #             | PreventiveCareServicesEstablishedOfficeVisit18AndUp
            #             | HomeHealthcareServices
            #             | AnnualWellnessVisit
            #         ),
            #     )
            #     if self.context == CONTEXT_REPORT
            #     else True
            # ),
        )

    def in_denominator(self) -> bool:
        """
        Denominator: Equals Initial Population

        Exclusions: Men with known AAA or history of AAA repair

        Exclude patients who are in hospice care.

        Exceptions: None
        """
        if not self.in_initial_population():
            return False

        if self.patient.hospice_within(self.timeframe):
            return False

        # if self.had_mastectomy():
        #     return False
        if self.had_aaa_repair(): # TO DO: defne
            return False

        return True

    def in_numerator(self) -> bool:
        """
        Numerator: Men with one AAA US screening 

        Exclusions: Not Applicable
        """
        if self.period_adjustment:
            period = self.timeframe
        else:
            period = self.timeframe.increased_by(
                months=-1 * self.EXTRA_SCREENING_MONTHS
            )
        record = (
            self.patient.imaging_reports.find(AaaScreeningUltrasound)
            # .within(period)
            .last()
        )
        if record:
            self._on_date = arrow.get(record["originalDate"])
            return True

        return False

    def compute_results(self) -> ProtocolResult:
        """
        Clinical recommendation: The USPSTF recommends 1-time screening for abdominal aortic 
        aneurysm (AAA) with ultrasonography in men aged 65 to 75 years who have ever smoked.

        U.S. Preventive Services Task Force (2019)
        Grade: B recommendation. The USPSTF recommends 1-time screening for abdominal aortic 
        aneurysm (AAA) with ultrasonography in men aged 65 to 75 years who have ever smoked.
        Grade: C recommendation. TMen aged 65 to 75 years who have never smoked. The USPSTF 
        recommends that clinicians selectively offer screening for AAA with ultrasonography in men 
        aged 65 to 75 years who have never smoked rather than routinely screening all men in this 
        group. Evidence indicates that the net benefit of screening all men in this group is small. 
        In determining whether this service is appropriate in individual cases, patients and 
        clinicians should consider the balance of benefits and harms on the basis of evidence 
        relevant to the patient's medical history, family history, other risk factors, and personal 
        values.
        Grade: D recommendation. The USPSTF recommends against routine screening for AAA with 
        ultrasonography in women who have never smoked and have no family history of AAA.
        Grade: I Statement. The USPSTF concludes that the current evidence is insufficient to assess 
        the balance of benefits and harms of screening for AAA with ultrasonography in women aged 65 
        to 75 years who have ever smoked or have a family history of AAA.
        """
        result = ProtocolResult()

        if self.in_denominator():
            first_name = self.patient.first_name
            extra_months = 0 if self.period_adjustment else self.EXTRA_SCREENING_MONTHS
            if self.in_numerator() and self._on_date:
                result.due_in = (
                    self._on_date.shift(
                        days=self.timeframe.duration, months=extra_months
                    )
                    - self.now
                ).days
                result.status = STATUS_SATISFIED
                result.add_narrative(
                    f"{first_name} had a screening abdominal aorta ultrasound {self.display_date(self._on_date)}."
                )
            else:
                result.due_in = -1
                result.status = STATUS_DUE
                result.add_narrative("No relevant exams found.")
                result.add_narrative(self.screening_interval_context())
                result.add_instruction_recommendation(
                    key="PLAN_RECOMMENDATION",
                    rank=1,
                    button="Plan",
                    patient=self.patient,
                    instruction=AaaScreeningUltrasound,
                    title="Discuss screening ultrasound",
                )
                result.add_imaging_recommendation(
                    key="IMAGING_RECOMMENDATION",
                    rank=2,
                    button="Order",
                    patient=self.patient,
                    imaging=AaaScreeningUltrasound,
                    title="Order abdominal aorta ultrasound for aneurysm screening",
                    context={"conditions": [[EncounterForAaaScreening]]},
                )
        else:
            result.due_in = self.first_due_in()

        return result
