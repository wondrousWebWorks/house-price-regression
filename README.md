# Predicting House Prices Using Regression

A fictional individual, Jane Doe, has received an inheritance from a deceased great-grandfather. Included in the heritage are four houses located in Ames, Iowa. Although Jane has an excellent understanding of property prices in her own state and residential area, she fears that basing her estimates for property worth on her current knowledge might lead to inaccurate appraisals. What makes a house desirable and valuable where she comes from might not be the same in Ames, Iowa. 

Jane needs help if she is to maximise the sales price for the inherited properties. She decides to ask me, a Junior Data Practitioner, for help. Her reasons for doing so are two-fold:

1. She would rather give a friend much-needed exposure and experience than approaching a stranger and 
2. She also doesn't know the worth of the properties and does not want to take the risk of spending too much money without an idea of the possible return on her expenses.

## 1. Project Requirements

Jane made her requirements clear and expects a level of service equivalent to that of established Data Practitioners. There is potentially a decent amount of money to be made or lost when selling the four properties. The two requirements are outlined below.

### 1.1 Visualise data and determine which features contribute most to house prices in Ames, Iowa.

- Inspect the data related to house prices.
- Perform a correlation study to confirm that identified features are accurate and find any that were missed during data analysis.
- Plot the main variables to visualise insights.

### 1.2 Implement a way to use these features to predict the value of a house.

- Build different regression models to predict house prices based on identified variables.
- Perform validation on models to improve their performance.
- Compare the prediction results of all models to identify the best one.

From a Data Practitioner perspective, the **features** affecting house prices are **labels**, while the **house price** is the **target** column in the dataset.

## 2. Dataset Content

> The dataset was taken from the **House Prices - Advanced Regression Techniques** competion page on [Kaggle](https://www.kaggle.com/c/house-prices-advanced-regression-techniques/overview "House Price Regression page on Kaggle").

This dataset contains 79 explanatory variables which describe a plethory of aspects of residential homes in Ames, Iowa. Although any number of features can be chosen as the target variable, our fictious requirement is being able to predict the house price. Another requirement is identifying which features influence house prices in this particular district most. Exploratory Data Analysis is used to identify these features.

<details>
<summary>Click to expand the data set!</summary>

<table>
<thead>
  <tr>
    <th>Variable</th>
    <th>Meaning</th>
    <th>Units</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>MSSubClass</td>
    <td>Identifies the type of dwelling involved in the sale</td>
    <td>
        <table>
            <tr>
                <td>20 1-STORY 1946 & NEWER ALL STYLES</td>
            </tr>
            <tr>
                <td>30	1-STORY 1945 & OLDER</td>
            </tr>
            <tr>
                <td>40	1-STORY W/FINISHED ATTIC ALL AGES</td>
            </tr>
            <tr>
                <td>45	1-1/2 STORY - UNFINISHED ALL AGES</td>
            </tr>
            <tr>
                <td>50	1-1/2 STORY FINISHED ALL AGES</td>
            </tr>
            <tr>
                <td>60	2-STORY 1946 & NEWER</td>
            </tr>
            <tr>
                <td>70	2-STORY 1945 & OLDER</td>
            </tr>
            <tr>
                <td>75	2-1/2 STORY ALL AGES</td>
            </tr>
            <tr>
                <td>80	SPLIT OR MULTI-LEVEL</td>
            </tr>
            <tr>
                <td>85	SPLIT FOYER</td>
            </tr>
            <tr>
                <td>90	DUPLEX - ALL STYLES AND AGES</td>
            </tr>
            <tr>
                <td>120	1-STORY PUD (Planned Unit Development) - 1946 & NEWER</td>
            </tr>
            <tr>
                <td>150	1-1/2 STORY PUD - ALL AGES</td>
            </tr>
            <tr>
                <td>160	2-STORY PUD - 1946 & NEWER</td>
            </tr>
            <tr>
                <td>180	PUD - MULTILEVEL - INCL SPLIT LEV/FOYER</td>
            </tr>
            <tr>
                <td>190	2 FAMILY CONVERSION - ALL STYLES AND AGES</td>
            </tr>
        </table> 
       </td>
  </tr>
  <tr>
    <td>MSZoning</td>
    <td>Identifies the general zoning classification of the sale</td>
    <td>
        <table>
            <tr>
                <td>A	Agriculture</td>
            </tr>
            <tr>
                <td>C	Commercial</td>
            </tr>
            <tr>
                <td>FV	Floating Village Residential</td>
            </tr>
            <tr>
                <td>I	Industrial</td>
            </tr>
            <tr>
                <td>RH	Residential High Density</td>
            </tr>
            <tr>
                <td>RL	Residential Low Density</td>
            </tr>
            <tr>
                <td>RP	Residential Low Density Park</td>
            </tr>
            <tr>
                <td>RM	Residential Medium Density</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>LotFrontage</td>
    <td>Linear feet of street connected to property</td>
    <td>Feet</td>
  </tr>
  <tr>
    <td>LotArea</td>
    <td>Lot size in square feet</td>
    <td>Square Feet</td>
  </tr>
  <tr>
    <td>Street</td>
    <td>Type of road access to property</td>
    <td>
        <table>
            <tr>
                <td>Grvl	Gravel</td>
            </tr>
            <tr>
                <td>Pave	Paved</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>Alley</td>
    <td>Type of alley access to property</td>
    <td>
        <table>
            <tr>
                <td>Grvl	Gravel</td>
            </tr>
            <tr>
                <td>Pave	Paved</td>
            </tr>
            <tr>
                <td>NA 	No alley access</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>LotShape</td>
    <td>General shape of property</td>
    <td>
        <table>
            <tr>
                <td>Reg	Regular</td>
            </tr>
            <tr>
                <td>IR1	Slightly irregular</td>
            </tr>
            <tr>
                <td>IR2	Moderately Irregular</td>
            </tr>
            <tr>
                <td>IR3	Irregular</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>LandContour</td>
    <td>Flatness of the property</td>
    <td>
        <table>
            <tr>
                <td>Lvl	Near Flat/Level</td>
            </tr>
            <tr>
                <td>Bnk	Banked - Quick and significant rise from street grade to building</td>
            </tr>
            <tr>
                <td>HLS	Hillside - Significant slope from side to side</td>
            </tr>
            <tr>
                <td>Low	Depression</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>Utilities</td>
    <td>Type of utilities available</td>
    <td>
        <table>
            <tr>
                <td>AllPub	All public Utilities (E,G,W,& S)</td>
            </tr>
            <tr>
                <td>NoSewr	Electricity, Gas, and Water (Septic Tank)</td>
            </tr>
            <tr>
                <td>NoSeWa	Electricity and Gas Only</td>
            </tr>
            <tr>
                <td>ELO	Electricity only</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>LotConfig</td>
    <td>Lot configuration</td>
    <td>
        <table>
            <tr>
                <td>Inside	Inside lot</td>
            </tr>
            <tr>
                <td>Corner	Corner lot</td>
            </tr>
            <tr>
                <td>CulDSac	Cul-de-sac</td>
            </tr>
            <tr>
                <td>FR2	Frontage on 2 sides of property</td>
            </tr>
            <tr>
                <td>FR3	Frontage on 3 sides of property</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>LandSlope</td>
    <td>Slope of property</td>
    <td>
        <table>
            <tr>
                <td>Gtl	Gentle slope</td>
            </tr>
            <tr>
                <td>Mod	Moderate Slope</td>
            </tr>
            <tr>
                <td>Sev	Severe Slope</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>Neighborhood</td>
    <td>Physical locations within Ames city limits</td>
    <td>
        <table>
            <tr>
                <td>Blmngtn	Bloomington Heights</td>
            </tr>
            <tr>
                <td>Blueste	Bluestem</td>
            </tr>
            <tr>
                <td>BrDale	Briardale</td>
            </tr>
            <tr>
                <td>BrkSide	Brookside</td>
            </tr>
            <tr>
                <td>ClearCr	Clear Creek</td>
            </tr>
            <tr>
                <td>CollgCr	College Creek</td>
            </tr>
            <tr>
                <td>Crawfor	Crawford</td>
            </tr>
            <tr>
                <td>Edwards	Edwards</td>
            </tr>
            <tr>
                <td>Gilbert	Gilbert</td>
            </tr>
            <tr>
                <td>IDOTRR	Iowa DOT and Rail Road</td>
            </tr>
            <tr>
                <td>MeadowV	Meadow Village</td>
            </tr>
            <tr>
                <td>Mitchel	Mitchell</td>
            </tr>
            <tr>
                <td>Names	North Ames</td>
            </tr>
            <tr>
                <td>NoRidge	Northridge</td>
            </tr>
            <tr>
                <td>NPkVill	Northpark Villa</td>
            </tr>
            <tr>
                <td>NridgHt	Northridge Heights</td>
            </tr>
            <tr>
                <td>NWAmes	Northwest Ames</td>
            </tr>
            <tr>
                <td>OldTown	Old Town</td>
            </tr>
           <tr>
                <td>SWISU	South & West of Iowa State University</td>
            </tr>
           <tr>
                <td>Sawyer	Sawyer</td>
            </tr>
           <tr>
                <td>SawyerW	Sawyer West</td>
            </tr>
           <tr>
                <td>Somerst	Somerset</td>
            </tr>
           <tr>
                <td>StoneBr	Stone Brook</td>
            </tr>
           <tr>
                <td>Timber	Timberland</td>
            </tr>
           <tr>
                <td>Veenker	Veenker</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>Condition1</td>
    <td>Proximity to various conditions</td>
    <td>
        <table>
            <tr>
                <td>Artery	Adjacent to arterial street</td>
            </tr>
            <tr>
                <td>Feedr	Adjacent to feeder street</td>
            </tr>
            <tr>
                <td>Norm	Normal	</td>
            </tr>
            <tr>
                <td>RRNn	Within 200' of North-South Railroad</td>
            </tr>
            <tr>
                <td>RRAn	Adjacent to North-South Railroad</td>
            </tr>
            <tr>
                <td>PosN	Near positive off-site feature--park, greenbelt, etc.</td>
            </tr>
            <tr>
                <td>PosA	Adjacent to postive off-site feature</td>
            </tr>
            <tr>
                <td>RRNe	Within 200' of East-West Railroad</td>
            </tr>
            <tr>
                <td>RRAe	Adjacent to East-West Railroad</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>Condition2</td>
    <td>Proximity to various conditions (if more than one is present)</td>
     <td>
        <table>
            <tr>
                <td>Artery	Adjacent to arterial street</td>
            </tr>
            <tr>
                <td>Feedr	Adjacent to feeder street</td>
            </tr>
            <tr>
                <td>Norm	Normal	</td>
            </tr>
            <tr>
                <td>RRNn	Within 200' of North-South Railroad</td>
            </tr>
            <tr>
                <td>RRAn	Adjacent to North-South Railroad</td>
            </tr>
            <tr>
                <td>PosN	Near positive off-site feature--park, greenbelt, etc.</td>
            </tr>
            <tr>
                <td>PosA	Adjacent to postive off-site feature</td>
            </tr>
            <tr>
                <td>RRNe	Within 200' of East-West Railroad</td>
            </tr>
            <tr>
                <td>RRAe	Adjacent to East-West Railroad</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>BldgType</td>
    <td>Type of dwelling</td>
     <td>
        <table>
            <tr>
                <td>1Fam	Single-family Detached</td>
            </tr>
            <tr>
                <td>2FmCon	Two-family Conversion; originally built as one-family dwelling</td>
            </tr>
            <tr>
                <td>Duplx	Duplex</td>
            </tr>
            <tr>
                <td>TwnhsE	Townhouse End Unit</td>
            </tr>
            <tr>
                <td>TwnhsI	Townhouse Inside Unit</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>HouseStyle</td>
    <td>Style of dwelling</td>
     <td>
        <table>
            <tr>
                <td>1Story	One story</td>
            </tr>
            <tr>
                <td>1.5Fin	One and one-half story: 2nd level finished</td>
            </tr>
            <tr>
                <td>1.5Unf	One and one-half story: 2nd level unfinished</td>
            </tr>
            <tr>
                <td>2Story	Two story</td>
            </tr>
            <tr>
                <td>2.5Fin	Two and one-half story: 2nd level finished</td>
            </tr>
            <tr>
                <td>2.5Unf	Two and one-half story: 2nd level unfinished</td>
            </tr>
            <tr>
                <td>SFoyer	Split Foyer</td>
            </tr>
            <tr>
                <td>SLvl	Split Level</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>OverallQual</td>
    <td>Rates the overall material and finish of the house</td>
     <td>
        <table>
            <tr>
                <td>10	Very Excellent</td>
            </tr>
            <tr>
                <td>9	Excellent</td>
            </tr>
            <tr>
                <td>8	Very Good</td>
            </tr>
            <tr>
                <td>7	Good</td>
            </tr>
            <tr>
                <td>6	Above Average</td>
            </tr>
            <tr>
                <td>5	Average</td>
            </tr>
            <tr>
                <td>4	Below Average</td>
            </tr>
            <tr>
                <td>3	Fair</td>
            </tr>
            <tr>
                <td>2	Poor</td>
            </tr>
            <tr>
                <td>1	Very Poor</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>OverallCond</td>
    <td>Rates the overall condition of the house</td>
     <td>
        <table>
            <tr>
                <td>10	Very Excellent</td>
            </tr>
            <tr>
                <td>9	Excellent</td>
            </tr>
            <tr>
                <td>8	Very Good</td>
            </tr>
            <tr>
                <td>7	Good</td>
            </tr>
            <tr>
                <td>6	Above Average</td>
            </tr>
            <tr>
                <td>5	Average</td>
            </tr>
            <tr>
                <td>4	Below Average</td>
            </tr>
            <tr>
                <td>3	Fair</td>
            </tr>
            <tr>
                <td>2	Poor</td>
            </tr>
            <tr>
                <td>1	Very Poor</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>YearBuilt</td>
    <td>Original construction date</td>
     <td>
        <table>
            <tr>
                <td>Date</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>YearRemodAdd</td>
    <td>Remodel date (same as construction date if no remodeling or additions)</td>
     <td>
        <table>
            <tr>
                <td>Date</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>RoofStyle</td>
    <td>Type of roof</td>
     <td>
        <table>
            <tr>
                <td>Flat	Flat</td>
            </tr>
            <tr>
                <td>Gable	Gable</td>
            </tr>
            <tr>
                <td>Gambrel	Gabrel (Barn)</td>
            </tr>
            <tr>
                <td>Hip	Hip</td>
            </tr>
            <tr>
                <td>Mansard	Mansard</td>
            </tr>
            <tr>
                <td>Shed	Shed</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>RoofMatl</td>
    <td>Roof material</td>
     <td>
        <table>
            <tr>
                <td>ClyTile	Clay or Tile</td>
            </tr>
            <tr>
                <td>CompShg	Standard (Composite) Shingle</td>
            </tr>
            <tr>
                <td>Membran	Membrane</td>
            </tr>
            <tr>
                <td>Metal	Metal</td>
            </tr>
            <tr>
                <td>Roll	Roll</td>
            </tr>
            <tr>
                <td>Tar&Grv	Gravel & Tar</td>
            </tr>
            <tr>
                <td>WdShake	Wood Shakes</td>
            </tr>
            <tr>
                <td>WdShngl	Wood Shingles</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>Exterior1st</td>
    <td>Exterior covering on house</td>
     <td>
        <table>
            <tr>
                <td>AsbShng	Asbestos Shingles</td>
            </tr>
            <tr>
                <td>AsphShn	Asphalt Shingles</td>
            </tr>
            <tr>
                <td>BrkComm	Brick Common</td>
            </tr>
            <tr>
                <td>BrkFace	Brick Face</td>
            </tr>
            <tr>
                <td>CBlock	Cinder Block</td>
            </tr>
            <tr>
                <td>CemntBd	Cement Board</td>
            </tr>
            <tr>
                <td>HdBoard	Hard Board</td>
            </tr>
            <tr>
                <td>ImStucc	Imitation Stucco</td>
            </tr>
            <tr>
                <td>MetalSd	Metal Siding</td>
            </tr>
            <tr>
                <td>Other	Other</td>
            </tr>
            <tr>
                <td>Plywood	Plywood</td>
            </tr>
            <tr>
                <td>PreCast	PreCast</td>
            </tr>
            <tr>
                <td>Stone	Stone</td>
            </tr>
            <tr>
                <td>Stucco	Stucco</td>
            </tr>
            <tr>
                <td>VinylSd	Vinyl Siding</td>
            </tr>
            <tr>
                <td>Wd Sdng	Wood Siding</td>
            </tr>
            <tr>
                <td>WdShing	Wood Shingles</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>Exterior2nd</td>
    <td>Exterior covering on house (if more than one material)</td>
     <td>
        <table>
            <tr>
                <td>AsbShng	Asbestos Shingles</td>
            </tr>
            <tr>
                <td>AsphShn	Asphalt Shingles</td>
            </tr>
            <tr>
                <td>BrkComm	Brick Common</td>
            </tr>
            <tr>
                <td>BrkFace	Brick Face</td>
            </tr>
            <tr>
                <td>CBlock	Cinder Block</td>
            </tr>
            <tr>
                <td>CemntBd	Cement Board</td>
            </tr>
            <tr>
                <td>HdBoard	Hard Board</td>
            </tr>
            <tr>
                <td>ImStucc	Imitation Stucco</td>
            </tr>
            <tr>
                <td>MetalSd	Metal Siding</td>
            </tr>
            <tr>
                <td>Other	Other</td>
            </tr>
            <tr>
                <td>Plywood	Plywood</td>
            </tr>
            <tr>
                <td>PreCast	PreCast</td>
            </tr>
            <tr>
                <td>Stone	Stone</td>
            </tr>
            <tr>
                <td>Stucco	Stucco</td>
            </tr>
            <tr>
                <td>VinylSd	Vinyl Siding</td>
            </tr>
            <tr>
                <td>Wd Sdng	Wood Siding</td>
            </tr>
            <tr>
                <td>WdShing	Wood Shingles</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>MasVnrType</td>
    <td>Masonry veneer type</td>
     <td>
        <table>
            <tr>
                <td>BrkCmn	Brick Common</td>
            </tr>
            <tr>
                <td>BrkFace	Brick Face</td>
            </tr>
            <tr>
                <td>CBlock	Cinder Block</td>
            </tr>
            <tr>
                <td>None	None</td>
            </tr>
            <tr>
                <td>Stone	Stone</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>MasVnrArea</td>
    <td>Masonry veneer area in square feet</td>
     <td>
        <table>
            <tr>
                <td>Square feet</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>ExterQual</td>
    <td>Evaluates the quality of the material on the exterior</td>
     <td>
        <table>
            <tr>
                <td>Ex	Excellent</td>
            </tr>
            <tr>
                <td>Gd	Good</td>
            </tr>
            <tr>
                <td>TA	Average/Typical</td>
            </tr>
            <tr>
                <td>Fa	Fair</td>
            </tr>
            <tr>
                <td>Po	Poor</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>ExterCond</td>
    <td>Evaluates the present condition of the material on the exterior</td>
     <td>
        <table>
            <tr>
                <td>Ex	Excellent</td>
            </tr>
            <tr>
                <td>Gd	Good</td>
            </tr>
            <tr>
                <td>TA	Average/Typical</td>
            </tr>
            <tr>
                <td>Fa	Fair</td>
            </tr>
            <tr>
                <td>Po	Poor</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>Foundation</td>
    <td>Type of foundation</td>
     <td>
        <table>
            <tr>
                <td>BrkTil	Brick & Tile</td>
            </tr>
            <tr>
                <td>CBlock	Cinder Block</td>
            </tr>
            <tr>
                <td>PConc	Poured Contrete</td>
            </tr>
            <tr>
                <td>Slab	Slab</td>
            </tr>
            <tr>
                <td>Stone	Stone</td>
            </tr>
            <tr>
                <td>Wood	Wood</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>BsmtQual</td>
    <td>Evaluates the height of the basement</td>
     <td>
        <table>
            <tr>
                <td>Ex	Excellent (100+ inches)</td>
            </tr>
            <tr>
                <td>Gd	Good (90-99 inches)</td>
            </tr>
            <tr>
                <td>TA	Typical (80-89 inches)</td>
            </tr>
            <tr>
                <td>Fa	Fair (70-79 inches)</td>
            </tr>
            <tr>
                <td>Po	Poor (<70 inches)</td>
            </tr>
           <tr>
                <td>NA	No Basement</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>BsmtCond</td>
    <td>Evaluates the general condition of the basement</td>
     <td>
        <table>
            <tr>
                <td>Ex	Excellent</td>
            </tr>
            <tr>
                <td>Gd	Good</td>
            </tr>
            <tr>
                <td>TA	Typical - slight dampness allowed</td>
            </tr>
            <tr>
                <td>Fa	Fair - dampness or some cracking or settling</td>
            </tr>
            <tr>
                <td>Po	Poor - Severe cracking, settling, or wetness</td>
            </tr>
            <tr>
                <td>NA	No Basement</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>BsmtExposure</td>
    <td>Refers to walkout or garden level walls</td>
     <td>
        <table>
            <tr>
                <td>Gd	Good Exposure</td>
            </tr>
            <tr>
                <td>Av	Average Exposure (split levels or foyers typically score average or above)</td>
            </tr>
            <tr>
                <td>Mn	Mimimum Exposure</td>
            </tr>
            <tr>
                <td>No	No Exposure</td>
            </tr>
            <tr>
                <td>NA	No Basement</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>BsmtFinType1</td>
    <td>Rating of basement finished area</td>
     <td>
        <table>
            <tr>
                <td>GLQ	Good Living Quarters</td>
            </tr>
            <tr>
                <td>ALQ	Average Living Quarters</td>
            </tr>
            <tr>
                <td>BLQ	Below Average Living Quarters</td>
            </tr>
            <tr>
                <td>Rec	Average Rec Room</td>
            </tr>
            <tr>
                <td>LwQ	Low Quality</td>
            </tr>
            <tr>
                <td>Unf	Unfinshed</td>
            </tr>
            <tr>
                <td>NA	No Basement</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>BsmtFinSF2</td>
    <td>Type 2 finished square feet</td>
     <td>
        <table>
            <tr>
                <td>Square feet</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>BsmtUnfSF</td>
    <td>Unfinished square feet of basement area</td>
     <td>
        <table>
            <tr>
                <td>Square feet</td>
            </tr>
        </table> 
    </td>
  </tr>
 <tr>
    <td>TotalBsmtSF</td>
    <td>Total square feet of basement area</td>
     <td>
        <table>
            <tr>
                <td>Square feet</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>Heating</td>
    <td>Type of heating</td>
     <td>
        <table>
            <tr>
                <td>Floor	Floor Furnace</td>
            </tr>
            <tr>
                <td>GasA	Gas forced warm air furnace</td>
            </tr>
            <tr>
                <td>GasW	Gas hot water or steam heat</td>
            </tr>
            <tr>
                <td>Grav	Gravity furnace</td>
            </tr>
            <tr>
                <td>OthW	Hot water or steam heat other than gas</td>
            </tr>
            <tr>
                <td>Wall	Wall furnace</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>HeatingQC</td>
    <td>Heating quality and condition</td>
     <td>
        <table>
            <tr>
                <td>Ex	Excellent</td>
            </tr>
            <tr>
                <td>Gd	Good</td>
            </tr>
            <tr>
                <td>TA	Average/Typical</td>
            </tr>
            <tr>
                <td>Fa	Fair</td>
            </tr>
            <tr>
                <td>Po	Poor</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>CentralAir</td>
    <td>Central air conditioning</td>
     <td>
        <table>
            <tr>
                <td>N	No</td>
            </tr>
            <tr>
                <td>Y	Yes</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>Electrical</td>
    <td>Electrical system</td>
     <td>
        <table>
            <tr>
                <td>SBrkr	Standard Circuit Breakers & Romex</td>
            </tr>
            <tr>
                <td>FuseA	Fuse Box over 60 AMP and all Romex wiring (Average)</td>
            </tr>
            <tr>
                <td>FuseF	60 AMP Fuse Box and mostly Romex wiring (Fair)</td>
            </tr>
            <tr>
                <td>FuseP	60 AMP Fuse Box and mostly knob & tube wiring (poor)</td>
            </tr>
            <tr>
                <td>Mix	Mixed</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>1stFlrSF</td>
    <td>First Floor square feet</td>
     <td>
        <table>
            <tr>
                <td>Square feet</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>2ndFlrSF</td>
    <td>Second floor square feet</td>
     <td>
        <table>
            <tr>
                <td>Square feet</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>LowQualFinSF</td>
    <td>Low quality finished square feet (all floors)</td>
     <td>
        <table>
            <tr>
                <td>Square feet</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>GrLivArea</td>
    <td>Above grade (ground) living area square feet</td>
     <td>
        <table>
            <tr>
                <td>Square feet</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>BsmtFullBath</td>
    <td>Basement full bathrooms</td>
     <td>
        <table>
            <tr>
                <td>Quantity</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>BsmtHalfBath</td>
    <td>Basement half bathrooms</td>
     <td>
        <table>
            <tr>
                <td>Quantity</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>FullBath</td>
    <td>Full bathrooms above grade</td>
     <td>
        <table>
            <tr>
                <td>Quantity</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>HalfBath</td>
    <td>Half baths above grade</td>
     <td>
        <table>
            <tr>
                <td>Quantity</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>Bedroom</td>
    <td>Bedrooms above grade (does NOT include basement bedrooms)</td>
     <td>
        <table>
            <tr>
                <td>Quantity</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>Kitchen</td>
    <td>Kitchens above grade</td>
     <td>
        <table>
            <tr>
                <td>Quantity</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>KitchenQual</td>
    <td>Kitchen quality</td>
     <td>
        <table>
            <tr>
                <td>Ex	Excellent</td>
            </tr>
            <tr>
                <td>Gd	Good</td>
            </tr>
            <tr>
                <td>TA	Typical/Average</td>
            </tr>
            <tr>
                <td>Fa	Fair</td>
            </tr>
            <tr>
                <td>Po	Poor</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>TotRmsAbvGrd</td>
    <td>Total rooms above grade (does not include bathrooms)</td>
     <td>
        <table>
            <tr>
                <td>Quantity</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>Functional</td>
    <td>Home functionality (Assume typical unless deductions are warranted)</td>
     <td>
        <table>
            <tr>
                <td>Typ	Typical Functionality</td>
            </tr>
            <tr>
                <td>Min1	Minor Deductions 1</td>
            </tr>
            <tr>
                <td>Min2	Minor Deductions 2</td>
            </tr>
            <tr>
                <td>Mod	Moderate Deductions</td>
            </tr>
            <tr>
                <td>Maj1	Major Deductions 1</td>
            </tr>
            <tr>
                <td>Maj2	Major Deductions 2</td>
            </tr>
            <tr>
                <td>Sev	Severely Damaged</td>
            </tr>
            <tr>
                <td>Sal	Salvage only</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>Fireplaces</td>
    <td>Number of fireplaces</td>
     <td>
        <table>
            <tr>
                <td>Quantity</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>FireplaceQu</td>
    <td>Fireplace quality</td>
     <td>
        <table>
            <tr>
                <td>Ex	Excellent - Exceptional Masonry Fireplace</td>
            </tr>
            <tr>
                <td>Gd	Good - Masonry Fireplace in main level</td>
            </tr>
            <tr>
                <td>TA	Average - Prefabricated Fireplace in main living area or Masonry Fireplace in basement</td>
            </tr>
            <tr>
                <td>Fa	Fair - Prefabricated Fireplace in basement</td>
            </tr>
            <tr>
                <td>Po	Poor - Ben Franklin Stove</td>
            </tr>
            <tr>
                <td>NA	No Fireplace</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>GarageType</td>
    <td>Garage location</td>
     <td>
        <table>
            <tr>
                <td>2Types	More than one type of garage</td>
            </tr>
            <tr>
                <td>Attchd	Attached to home</td>
            </tr>
            <tr>
                <td>Basment	Basement Garage</td>
            </tr>
            <tr>
                <td>BuiltIn	Built-In (Garage part of house - typically has room above garage)</td>
            </tr>
            <tr>
                <td>CarPort	Car Port</td>
            </tr>
            <tr>
                <td>Detchd	Detached from home</td>
            </tr>
            <tr>
                <td>NA	No Garage</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>GarageYrBlt</td>
    <td>Year garage was built</td>
     <td>
        <table>
            <tr>
                <td>Date</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>GarageFinish</td>
    <td>Interior finish of the garage</td>
     <td>
        <table>
            <tr>
                <td>Fin	Finished</td>
            </tr>
            <tr>
                <td>RFn	Rough Finished</td>
            </tr>
            <tr>
                <td>Unf	Unfinished</td>
            </tr>
            <tr>
                <td>NA	No Garage</td>
            </tr>
            <tr>
                <td></td>
            </tr>
            <tr>
                <td></td>
            </tr>
            <tr>
                <td></td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>GarageCars</td>
    <td>Size of garage in car capacity</td>
     <td>
        <table>
            <tr>
                <td>Car capacity</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>GarageArea</td>
    <td>Size of garage in square feet</td>
     <td>
        <table>
            <tr>
                <td>Square feet</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>GarageQual</td>
    <td>Garage quality</td>
     <td>
        <table>
            <tr>
                <td>Ex	Excellent</td>
            </tr>
            <tr>
                <td>Gd	Good</td>
            </tr>
            <tr>
                <td>TA	Typical/Average</td>
            </tr>
            <tr>
                <td>Fa	Fair</td>
            </tr>
            <tr>
                <td>Po	Poor</td>
            </tr>
            <tr>
                <td>NA	No Garage</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>GarageCond</td>
    <td>Garage condition</td>
     <td>
        <table>
            <tr>
                <td>Ex	Excellent</td>
            </tr>
            <tr>
                <td>Gd	Good</td>
            </tr>
            <tr>
                <td>TA	Typical/Average</td>
            </tr>
            <tr>
                <td>Fa	Fair</td>
            </tr>
            <tr>
                <td>Po	Poor</td>
            </tr>
            <tr>
                <td>NA	No Garage</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>PavedDrive</td>
    <td>Paved driveway</td>
     <td>
        <table>
            <tr>
                <td>Y	Paved</td>
            </tr>
            <tr>
                <td>P	Partial Pavement</td>
            </tr>
            <tr>
                <td>N	Dirt/Gravel</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>WoodDeckSF</td>
    <td>Wood deck area in square feet</td>
     <td>
        <table>
            <tr>
                <td>Square feet</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>OpenPorchSF</td>
    <td>Open porch area in square feet</td>
     <td>
        <table>
            <tr>
                <td>Square feet</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>EnclosedPorch</td>
    <td>Enclosed porch area in square feet</td>
     <td>
        <table>
            <tr>
                <td>Square feet</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>3SsnPorch</td>
    <td>Three season porch area in square feet</td>
     <td>
        <table>
            <tr>
                <td>Square feet</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>ScreenPorch</td>
    <td>Screen porch area in square feet</td>
     <td>
        <table>
            <tr>
                <td>Square feet</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>PoolArea</td>
    <td>Pool area in square feet</td>
     <td>
        <table>
            <tr>
                <td>Square feet</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>PoolQC</td>
    <td>Pool quality</td>
     <td>
        <table>
            <tr>
                <td>Ex	Excellent</td>
            </tr>
            <tr>
                <td>Gd	Good</td>
            </tr>
            <tr>
                <td>TA	Average/Typical</td>
            </tr>
            <tr>
                <td>Fa	Fair</td>
            </tr>
            <tr>
                <td>NA	No Pool</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>Fence</td>
    <td>Fence quality</td>
     <td>
        <table>
            <tr>
                <td>GdPrv	Good Privacy</td>
            </tr>
            <tr>
                <td>MnPrv	Minimum Privacy</td>
            </tr>
            <tr>
                <td>GdWo	Good Wood</td>
            </tr>
            <tr>
                <td>MnWw	Minimum Wood/Wire</td>
            </tr>
            <tr>
                <td>NA	No Fence</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>MiscFeature</td>
    <td>Miscellaneous feature not covered in other categories</td>
     <td>
        <table>
            <tr>
                <td>Elev	Elevator</td>
            </tr>
            <tr>
                <td>Gar2	2nd Garage (if not described in garage section)</td>
            </tr>
            <tr>
                <td>Othr	Other</td>
            </tr>
            <tr>
                <td>Shed	Shed (over 100 SF)</td>
            </tr>
            <tr>
                <td>TenC	Tennis Court</td>
            </tr>
            <tr>
                <td>NA	None</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>MiscVal</td>
    <td>$Value of miscellaneous feature</td>
     <td>
        <table>
            <tr>
                <td>Dollars</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>MoSold</td>
    <td>Month Sold (MM)</td>
     <td>
        <table>
            <tr>
                <td>Month</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>YrSold</td>
    <td>Year Sold (YYYY)</td>
     <td>
        <table>
            <tr>
                <td>Year</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>SaleType</td>
    <td>Type of sale</td>
     <td>
        <table>
            <tr>
                <td>WD 	Warranty Deed - Conventional</td>
            </tr>
            <tr>
                <td>CWD	Warranty Deed - Cash</td>
            </tr>
            <tr>
                <td>VWD	Warranty Deed - VA Loan</td>
            </tr>
            <tr>
                <td>New	Home just constructed and sold</td>
            </tr>
            <tr>
                <td>COD	Court Officer Deed/Estate</td>
            </tr>
            <tr>
                <td>Con	Contract 15% Down payment regular terms</td>
            </tr>
            <tr>
                <td>ConLw	Contract Low Down payment and low interest</td>
            </tr>
            <tr>
                <td>ConLI	Contract Low Interest</td>
            </tr>
            <tr>
                <td>ConLD	Contract Low Down</td>
            </tr>
            <tr>
                <td>Oth	Other</td>
            </tr>
        </table> 
    </td>
  </tr>
  <tr>
    <td>SaleCondition</td>
    <td>Condition of sale</td>
     <td>
        <table>
            <tr>
                <td>Normal	Normal Sale</td>
            </tr>
            <tr>
                <td>Abnorml	Abnormal Sale -  trade, foreclosure, short sale</td>
            </tr>
            <tr>
                <td>AdjLand	Adjoining Land Purchase</td>
            </tr>
            <tr>
                <td>Alloca	Allocation - two linked properties with separate deeds, typically condo with a garage unit</td>
            </tr>
            <tr>
                <td>Family	Sale between family members</td>
            </tr>
            <tr>
                <td>Partial	Home was not completed when last assessed (associated with New Homes)</td>
            </tr>
        </table> 
    </td>
  </tr>
</tbody>
</table>
</details>

## 3. Machine Learning (ML) Business Case

We have been tasked with identifying the features which most affect the price of houses in Ames, Iowa. Once these feature variable have been identified, they need to be used to train a ML model that can predict house prices with a certain degree of certainty.

### 3.1 Models

Prediction calls for the use of regression models. Though there are a variety of regression models to choose from, this study will focus on the following:

#### 3.1.1 Linear Regression Model

Linear regression is a Supervised Learning algorithm. It assumes a linear relationship between the input variables (x) and the single output variable (y). In essence, y can be calculated from a linear combination of the input variables (x). More information on the formulas used for Linear Regression can be found [here](https://machinelearningmastery.com/linear-regression-for-machine-learning/).

The existing [LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html) model from the Scikit Learn library will suit our purposes.

#### 3.1.2 Random Forest Regression Model

Random forest is also a Supervised Learning algorithm. An ensemble learning method for regression and classification is used. In our study, we will focus in its regression capabilities. A multitude of decision trees are built at training time and the class that is the mean prediction (regression) of the individual trees are generated as output.

A random forest is a meta-estimator which combines the result of multiple predictions and aggregates many decision trees. For information, please read [this](https://medium.com/swlh/random-forest-and-its-implementation-71824ced454f) Medium article.

We will use the [RandomForestRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html?highlight=randomforestregressor#sklearn.ensemble.RandomForestRegressor) model from the Scikit Learn library in our study.

## 4. Credits

- The **Churnometer** walkthrough project from Code Institute was referenced:
    - for the general project structure
    - to see how Streamlit apps are written
- [Hands-on Machine Learning with Scikit-Learn, Keras, and TensorFlow: Concepts, Tools, and Techniques to Build Intelligent Systems](https://www.amazon.co.uk/Hands-Machine-Learning-Scikit-Learn-TensorFlow-ebook/dp/B07XGF2G87/ref=tmm_kin_swatch_0?_encoding=UTF8&qid=1635230780&sr=8-1), Aurelien Geron, 2019
    - correlation
    - RandomizedSearchCV for model optimisation
