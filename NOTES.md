I worked through the quick start API. Successfully created a patient and patient appointment. I want to run this patient through the AAA screening protocol. In that spirit I opened the patient's chart, opened protocols and recorded a smoking history of Former User. Next I queried all observation and what I find is: none. So it appears that the Canvas tobacco questionnaire does not create a coded tobacco history AFAIK. 

Next step - create a new observation. 

Is there still hope to test an AAA screening protocol? Yes, as long as you can create the tobacco history observation. Unfortunately the documentation states: 

>Currently the Observation Create Endpoint can only be used to generate vital sign panels and vital signs.
>
>Although the observation endpoint houses many different Canvas models, currently, only vital signs and panels can be created through this endpoint.