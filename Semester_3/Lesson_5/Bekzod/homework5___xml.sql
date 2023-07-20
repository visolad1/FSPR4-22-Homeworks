<?xml version="1.0" encoding="UTF-8"?>
<sqlb_project>
  <db path="C:/Users/WINDOWS 10/Documents/Githome/semester3/lesson-5/world.db" readonly="0" foreign_keys="1" case_sensitive_like="0" temp_store="0" wal_autocheckpoint="1000" synchronous="2"/>
  <attached/>
  <window>
    <main_tabs open="structure query browser pragmas" current="1"/>
  </window>
  <tab_structure>
    <column_width id="0" width="300"/>
    <column_width id="1" width="0"/>
    <column_width id="2" width="110"/>
    <column_width id="3" width="3607"/>
    <column_width id="4" width="0"/>
    <expanded_item id="0" parent="1"/>
    <expanded_item id="1" parent="1"/>
    <expanded_item id="2" parent="1"/>
    <expanded_item id="3" parent="1"/>
  </tab_structure>
  <tab_browse>
    <current_table name="4,4:mainCity"/>
    <default_encoding codec=""/>
    <browse_table_settings>
      <table schema="main" name="City" show_row_id="0" encoding="" plot_x_axis="" unlock_view_pk="_rowid_">
        <sort/>
        <column_widths>
          <column index="1" value="45"/>
          <column index="2" value="217"/>
          <column index="3" value="104"/>
          <column index="4" value="156"/>
          <column index="5" value="88"/>
        </column_widths>
        <filter_values/>
        <conditional_formats/>
        <row_id_formats/>
        <display_formats/>
        <hidden_columns/>
        <plot_y_axes/>
        <global_filter/>
      </table>
    </browse_table_settings>
  </tab_browse>
  <tab_sql>
    <sql name="SQL 1">
      -- Task- 4 
      -- SELECT City.Name as City, Country.Name as Country, CountryLanguage.Language from city join Country on City.CountryCode = Country.Code JOIN CountryLanguage on  CountryLanguage.CountryCode = Country.Code;

      -- Task-5 
      -- SELECT count(City.Name) as City  from Country join city on Country.Code = City.CountryCode; 

      -- Task-6 
      -- SELECT Country.Name, Country.Population from Country JOIN city On Country.Code = City.CountryCode ORDER By Country.Population ASC; 

      -- Task-7 
      -- SELECT Country.Name as Country, city.Name as City , City.Population from Country join city on Country.Code = City.CountryCode where city.Population &gt; 500000 GROUP By 1 ORDER BY 3 ASC; 

      -- Task-8 
      -- SELECT Country.Name, count(CountryLanguage.Language) as Language from Country JOIN CountryLanguage on Country.Code = CountryLanguage.CountryCode GROUP By 1 ORDER By 2 Desc; 
    </sql>
    <current_tab id="0"/>
  </tab_sql>
</sqlb_project>

