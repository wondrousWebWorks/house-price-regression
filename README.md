# Predicting House Prices Using Regression

## Dataset Content

> The dataset was taken from the **House Prices - Advanced Regression Techniques** competion page on [Kaggle](https://www.kaggle.com/c/house-prices-advanced-regression-techniques/overview "House Price Regression page on Kaggle").

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
</tbody>
</table>