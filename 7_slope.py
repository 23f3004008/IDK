from bs4 import BeautifulSoup
import numpy as np
from datetime import datetime

# Paste your HTML string here from devtools
html_input = """<div class="d-flex flex-wrap gap-2 mb-2">
        <!--?lit$087395872$--><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-07-20</div>
            <div><!--?lit$087395872$-->Sat</div>
            <div><!--?lit$087395872$-->480</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-07-21</div>
            <div><!--?lit$087395872$-->Sun</div>
            <div><!--?lit$087395872$-->488</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-07-22</div>
            <div><!--?lit$087395872$-->Mon</div>
            <div><!--?lit$087395872$-->522</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-07-23</div>
            <div><!--?lit$087395872$-->Tue</div>
            <div><!--?lit$087395872$-->524</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-07-24</div>
            <div><!--?lit$087395872$-->Wed</div>
            <div><!--?lit$087395872$-->494</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-07-25</div>
            <div><!--?lit$087395872$-->Thu</div>
            <div><!--?lit$087395872$-->485</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-07-26</div>
            <div><!--?lit$087395872$-->Fri</div>
            <div><!--?lit$087395872$-->490</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-07-27</div>
            <div><!--?lit$087395872$-->Sat</div>
            <div><!--?lit$087395872$-->502</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-07-28</div>
            <div><!--?lit$087395872$-->Sun</div>
            <div><!--?lit$087395872$-->516</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-07-29</div>
            <div><!--?lit$087395872$-->Mon</div>
            <div><!--?lit$087395872$-->525</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-07-30</div>
            <div><!--?lit$087395872$-->Tue</div>
            <div><!--?lit$087395872$-->521</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-07-31</div>
            <div><!--?lit$087395872$-->Wed</div>
            <div><!--?lit$087395872$-->499</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-08-01</div>
            <div><!--?lit$087395872$-->Thu</div>
            <div><!--?lit$087395872$-->510</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-08-02</div>
            <div><!--?lit$087395872$-->Fri</div>
            <div><!--?lit$087395872$-->500</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-08-03</div>
            <div><!--?lit$087395872$-->Sat</div>
            <div><!--?lit$087395872$-->519</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-08-04</div>
            <div><!--?lit$087395872$-->Sun</div>
            <div><!--?lit$087395872$-->515</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-08-05</div>
            <div><!--?lit$087395872$-->Mon</div>
            <div><!--?lit$087395872$-->528</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-08-06</div>
            <div><!--?lit$087395872$-->Tue</div>
            <div><!--?lit$087395872$-->510</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-08-07</div>
            <div><!--?lit$087395872$-->Wed</div>
            <div><!--?lit$087395872$-->525</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-08-08</div>
            <div><!--?lit$087395872$-->Thu</div>
            <div><!--?lit$087395872$-->514</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-08-09</div>
            <div><!--?lit$087395872$-->Fri</div>
            <div><!--?lit$087395872$-->516</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-08-10</div>
            <div><!--?lit$087395872$-->Sat</div>
            <div><!--?lit$087395872$-->525</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-08-11</div>
            <div><!--?lit$087395872$-->Sun</div>
            <div><!--?lit$087395872$-->529</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-08-12</div>
            <div><!--?lit$087395872$-->Mon</div>
            <div><!--?lit$087395872$-->504</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-08-13</div>
            <div><!--?lit$087395872$-->Tue</div>
            <div><!--?lit$087395872$-->515</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-08-14</div>
            <div><!--?lit$087395872$-->Wed</div>
            <div><!--?lit$087395872$-->499</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-08-15</div>
            <div><!--?lit$087395872$-->Thu</div>
            <div><!--?lit$087395872$-->531</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-08-16</div>
            <div><!--?lit$087395872$-->Fri</div>
            <div><!--?lit$087395872$-->518</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-08-17</div>
            <div><!--?lit$087395872$-->Sat</div>
            <div><!--?lit$087395872$-->511</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-08-18</div>
            <div><!--?lit$087395872$-->Sun</div>
            <div><!--?lit$087395872$-->497</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-08-19</div>
            <div><!--?lit$087395872$-->Mon</div>
            <div><!--?lit$087395872$-->539</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-08-20</div>
            <div><!--?lit$087395872$-->Tue</div>
            <div><!--?lit$087395872$-->494</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-08-21</div>
            <div><!--?lit$087395872$-->Wed</div>
            <div><!--?lit$087395872$-->522</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-08-22</div>
            <div><!--?lit$087395872$-->Thu</div>
            <div><!--?lit$087395872$-->496</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-08-23</div>
            <div><!--?lit$087395872$-->Fri</div>
            <div><!--?lit$087395872$-->544</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-08-24</div>
            <div><!--?lit$087395872$-->Sat</div>
            <div><!--?lit$087395872$-->543</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-08-25</div>
            <div><!--?lit$087395872$-->Sun</div>
            <div><!--?lit$087395872$-->536</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-08-26</div>
            <div><!--?lit$087395872$-->Mon</div>
            <div><!--?lit$087395872$-->533</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-08-27</div>
            <div><!--?lit$087395872$-->Tue</div>
            <div><!--?lit$087395872$-->501</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-08-28</div>
            <div><!--?lit$087395872$-->Wed</div>
            <div><!--?lit$087395872$-->532</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-08-29</div>
            <div><!--?lit$087395872$-->Thu</div>
            <div><!--?lit$087395872$-->507</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-08-30</div>
            <div><!--?lit$087395872$-->Fri</div>
            <div><!--?lit$087395872$-->532</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-08-31</div>
            <div><!--?lit$087395872$-->Sat</div>
            <div><!--?lit$087395872$-->534</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-09-01</div>
            <div><!--?lit$087395872$-->Sun</div>
            <div><!--?lit$087395872$-->533</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-09-02</div>
            <div><!--?lit$087395872$-->Mon</div>
            <div><!--?lit$087395872$-->513</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-09-03</div>
            <div><!--?lit$087395872$-->Tue</div>
            <div><!--?lit$087395872$-->550</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-09-04</div>
            <div><!--?lit$087395872$-->Wed</div>
            <div><!--?lit$087395872$-->552</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-09-05</div>
            <div><!--?lit$087395872$-->Thu</div>
            <div><!--?lit$087395872$-->553</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-09-06</div>
            <div><!--?lit$087395872$-->Fri</div>
            <div><!--?lit$087395872$-->531</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-09-07</div>
            <div><!--?lit$087395872$-->Sat</div>
            <div><!--?lit$087395872$-->539</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-09-08</div>
            <div><!--?lit$087395872$-->Sun</div>
            <div><!--?lit$087395872$-->532</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-09-09</div>
            <div><!--?lit$087395872$-->Mon</div>
            <div><!--?lit$087395872$-->531</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-09-10</div>
            <div><!--?lit$087395872$-->Tue</div>
            <div><!--?lit$087395872$-->515</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-09-11</div>
            <div><!--?lit$087395872$-->Wed</div>
            <div><!--?lit$087395872$-->511</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-09-12</div>
            <div><!--?lit$087395872$-->Thu</div>
            <div><!--?lit$087395872$-->512</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-09-13</div>
            <div><!--?lit$087395872$-->Fri</div>
            <div><!--?lit$087395872$-->546</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-09-14</div>
            <div><!--?lit$087395872$-->Sat</div>
            <div><!--?lit$087395872$-->525</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-09-15</div>
            <div><!--?lit$087395872$-->Sun</div>
            <div><!--?lit$087395872$-->529</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-09-16</div>
            <div><!--?lit$087395872$-->Mon</div>
            <div><!--?lit$087395872$-->517</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-09-17</div>
            <div><!--?lit$087395872$-->Tue</div>
            <div><!--?lit$087395872$-->561</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-09-18</div>
            <div><!--?lit$087395872$-->Wed</div>
            <div><!--?lit$087395872$-->557</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-09-19</div>
            <div><!--?lit$087395872$-->Thu</div>
            <div><!--?lit$087395872$-->554</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-09-20</div>
            <div><!--?lit$087395872$-->Fri</div>
            <div><!--?lit$087395872$-->554</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-09-21</div>
            <div><!--?lit$087395872$-->Sat</div>
            <div><!--?lit$087395872$-->563</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-09-22</div>
            <div><!--?lit$087395872$-->Sun</div>
            <div><!--?lit$087395872$-->552</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-09-23</div>
            <div><!--?lit$087395872$-->Mon</div>
            <div><!--?lit$087395872$-->532</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-09-24</div>
            <div><!--?lit$087395872$-->Tue</div>
            <div><!--?lit$087395872$-->558</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-09-25</div>
            <div><!--?lit$087395872$-->Wed</div>
            <div><!--?lit$087395872$-->567</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-09-26</div>
            <div><!--?lit$087395872$-->Thu</div>
            <div><!--?lit$087395872$-->546</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-09-27</div>
            <div><!--?lit$087395872$-->Fri</div>
            <div><!--?lit$087395872$-->556</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-09-28</div>
            <div><!--?lit$087395872$-->Sat</div>
            <div><!--?lit$087395872$-->538</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-09-29</div>
            <div><!--?lit$087395872$-->Sun</div>
            <div><!--?lit$087395872$-->540</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-09-30</div>
            <div><!--?lit$087395872$-->Mon</div>
            <div><!--?lit$087395872$-->537</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-10-01</div>
            <div><!--?lit$087395872$-->Tue</div>
            <div><!--?lit$087395872$-->525</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-10-02</div>
            <div><!--?lit$087395872$-->Wed</div>
            <div><!--?lit$087395872$-->550</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-10-03</div>
            <div><!--?lit$087395872$-->Thu</div>
            <div><!--?lit$087395872$-->527</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-10-04</div>
            <div><!--?lit$087395872$-->Fri</div>
            <div><!--?lit$087395872$-->571</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-10-05</div>
            <div><!--?lit$087395872$-->Sat</div>
            <div><!--?lit$087395872$-->549</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-10-06</div>
            <div><!--?lit$087395872$-->Sun</div>
            <div><!--?lit$087395872$-->558</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-10-07</div>
            <div><!--?lit$087395872$-->Mon</div>
            <div><!--?lit$087395872$-->568</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-10-08</div>
            <div><!--?lit$087395872$-->Tue</div>
            <div><!--?lit$087395872$-->528</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-10-09</div>
            <div><!--?lit$087395872$-->Wed</div>
            <div><!--?lit$087395872$-->534</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-10-10</div>
            <div><!--?lit$087395872$-->Thu</div>
            <div><!--?lit$087395872$-->564</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-10-11</div>
            <div><!--?lit$087395872$-->Fri</div>
            <div><!--?lit$087395872$-->574</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-10-12</div>
            <div><!--?lit$087395872$-->Sat</div>
            <div><!--?lit$087395872$-->579</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-10-13</div>
            <div><!--?lit$087395872$-->Sun</div>
            <div><!--?lit$087395872$-->538</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-10-14</div>
            <div><!--?lit$087395872$-->Mon</div>
            <div><!--?lit$087395872$-->532</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-10-15</div>
            <div><!--?lit$087395872$-->Tue</div>
            <div><!--?lit$087395872$-->562</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-10-16</div>
            <div><!--?lit$087395872$-->Wed</div>
            <div><!--?lit$087395872$-->577</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-10-17</div>
            <div><!--?lit$087395872$-->Thu</div>
            <div><!--?lit$087395872$-->576</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-10-18</div>
            <div><!--?lit$087395872$-->Fri</div>
            <div><!--?lit$087395872$-->563</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-10-19</div>
            <div><!--?lit$087395872$-->Sat</div>
            <div><!--?lit$087395872$-->577</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-10-20</div>
            <div><!--?lit$087395872$-->Sun</div>
            <div><!--?lit$087395872$-->576</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-10-21</div>
            <div><!--?lit$087395872$-->Mon</div>
            <div><!--?lit$087395872$-->575</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-10-22</div>
            <div><!--?lit$087395872$-->Tue</div>
            <div><!--?lit$087395872$-->585</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-10-23</div>
            <div><!--?lit$087395872$-->Wed</div>
            <div><!--?lit$087395872$-->569</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-10-24</div>
            <div><!--?lit$087395872$-->Thu</div>
            <div><!--?lit$087395872$-->558</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-10-25</div>
            <div><!--?lit$087395872$-->Fri</div>
            <div><!--?lit$087395872$-->556</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-10-26</div>
            <div><!--?lit$087395872$-->Sat</div>
            <div><!--?lit$087395872$-->579</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-10-27</div>
            <div><!--?lit$087395872$-->Sun</div>
            <div><!--?lit$087395872$-->543</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-10-28</div>
            <div><!--?lit$087395872$-->Mon</div>
            <div><!--?lit$087395872$-->558</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-10-29</div>
            <div><!--?lit$087395872$-->Tue</div>
            <div><!--?lit$087395872$-->588</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-10-30</div>
            <div><!--?lit$087395872$-->Wed</div>
            <div><!--?lit$087395872$-->548</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-10-31</div>
            <div><!--?lit$087395872$-->Thu</div>
            <div><!--?lit$087395872$-->555</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-11-01</div>
            <div><!--?lit$087395872$-->Fri</div>
            <div><!--?lit$087395872$-->550</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-11-02</div>
            <div><!--?lit$087395872$-->Sat</div>
            <div><!--?lit$087395872$-->584</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-11-03</div>
            <div><!--?lit$087395872$-->Sun</div>
            <div><!--?lit$087395872$-->548</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-11-04</div>
            <div><!--?lit$087395872$-->Mon</div>
            <div><!--?lit$087395872$-->582</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-11-05</div>
            <div><!--?lit$087395872$-->Tue</div>
            <div><!--?lit$087395872$-->577</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-11-06</div>
            <div><!--?lit$087395872$-->Wed</div>
            <div><!--?lit$087395872$-->594</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-11-07</div>
            <div><!--?lit$087395872$-->Thu</div>
            <div><!--?lit$087395872$-->586</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-11-08</div>
            <div><!--?lit$087395872$-->Fri</div>
            <div><!--?lit$087395872$-->598</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-11-09</div>
            <div><!--?lit$087395872$-->Sat</div>
            <div><!--?lit$087395872$-->568</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-11-10</div>
            <div><!--?lit$087395872$-->Sun</div>
            <div><!--?lit$087395872$-->564</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-11-11</div>
            <div><!--?lit$087395872$-->Mon</div>
            <div><!--?lit$087395872$-->596</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-11-12</div>
            <div><!--?lit$087395872$-->Tue</div>
            <div><!--?lit$087395872$-->578</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-11-13</div>
            <div><!--?lit$087395872$-->Wed</div>
            <div><!--?lit$087395872$-->588</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-11-14</div>
            <div><!--?lit$087395872$-->Thu</div>
            <div><!--?lit$087395872$-->554</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-11-15</div>
            <div><!--?lit$087395872$-->Fri</div>
            <div><!--?lit$087395872$-->595</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-11-16</div>
            <div><!--?lit$087395872$-->Sat</div>
            <div><!--?lit$087395872$-->582</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-11-17</div>
            <div><!--?lit$087395872$-->Sun</div>
            <div><!--?lit$087395872$-->560</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-11-18</div>
            <div><!--?lit$087395872$-->Mon</div>
            <div><!--?lit$087395872$-->589</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-11-19</div>
            <div><!--?lit$087395872$-->Tue</div>
            <div><!--?lit$087395872$-->561</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-11-20</div>
            <div><!--?lit$087395872$-->Wed</div>
            <div><!--?lit$087395872$-->574</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-11-21</div>
            <div><!--?lit$087395872$-->Thu</div>
            <div><!--?lit$087395872$-->603</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-11-22</div>
            <div><!--?lit$087395872$-->Fri</div>
            <div><!--?lit$087395872$-->606</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-11-23</div>
            <div><!--?lit$087395872$-->Sat</div>
            <div><!--?lit$087395872$-->607</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-11-24</div>
            <div><!--?lit$087395872$-->Sun</div>
            <div><!--?lit$087395872$-->603</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-11-25</div>
            <div><!--?lit$087395872$-->Mon</div>
            <div><!--?lit$087395872$-->600</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-11-26</div>
            <div><!--?lit$087395872$-->Tue</div>
            <div><!--?lit$087395872$-->600</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-11-27</div>
            <div><!--?lit$087395872$-->Wed</div>
            <div><!--?lit$087395872$-->562</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-11-28</div>
            <div><!--?lit$087395872$-->Thu</div>
            <div><!--?lit$087395872$-->600</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-11-29</div>
            <div><!--?lit$087395872$-->Fri</div>
            <div><!--?lit$087395872$-->573</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-11-30</div>
            <div><!--?lit$087395872$-->Sat</div>
            <div><!--?lit$087395872$-->595</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-12-01</div>
            <div><!--?lit$087395872$-->Sun</div>
            <div><!--?lit$087395872$-->574</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-12-02</div>
            <div><!--?lit$087395872$-->Mon</div>
            <div><!--?lit$087395872$-->591</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-12-03</div>
            <div><!--?lit$087395872$-->Tue</div>
            <div><!--?lit$087395872$-->609</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-12-04</div>
            <div><!--?lit$087395872$-->Wed</div>
            <div><!--?lit$087395872$-->605</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-12-05</div>
            <div><!--?lit$087395872$-->Thu</div>
            <div><!--?lit$087395872$-->611</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-12-06</div>
            <div><!--?lit$087395872$-->Fri</div>
            <div><!--?lit$087395872$-->596</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-12-07</div>
            <div><!--?lit$087395872$-->Sat</div>
            <div><!--?lit$087395872$-->582</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-12-08</div>
            <div><!--?lit$087395872$-->Sun</div>
            <div><!--?lit$087395872$-->579</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-12-09</div>
            <div><!--?lit$087395872$-->Mon</div>
            <div><!--?lit$087395872$-->572</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-12-10</div>
            <div><!--?lit$087395872$-->Tue</div>
            <div><!--?lit$087395872$-->584</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-12-11</div>
            <div><!--?lit$087395872$-->Wed</div>
            <div><!--?lit$087395872$-->578</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-12-12</div>
            <div><!--?lit$087395872$-->Thu</div>
            <div><!--?lit$087395872$-->588</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-12-13</div>
            <div><!--?lit$087395872$-->Fri</div>
            <div><!--?lit$087395872$-->582</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-12-14</div>
            <div><!--?lit$087395872$-->Sat</div>
            <div><!--?lit$087395872$-->615</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-12-15</div>
            <div><!--?lit$087395872$-->Sun</div>
            <div><!--?lit$087395872$-->601</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-12-16</div>
            <div><!--?lit$087395872$-->Mon</div>
            <div><!--?lit$087395872$-->622</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-12-17</div>
            <div><!--?lit$087395872$-->Tue</div>
            <div><!--?lit$087395872$-->581</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-12-18</div>
            <div><!--?lit$087395872$-->Wed</div>
            <div><!--?lit$087395872$-->613</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-12-19</div>
            <div><!--?lit$087395872$-->Thu</div>
            <div><!--?lit$087395872$-->585</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-12-20</div>
            <div><!--?lit$087395872$-->Fri</div>
            <div><!--?lit$087395872$-->603</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-12-21</div>
            <div><!--?lit$087395872$-->Sat</div>
            <div><!--?lit$087395872$-->586</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-12-22</div>
            <div><!--?lit$087395872$-->Sun</div>
            <div><!--?lit$087395872$-->591</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-12-23</div>
            <div><!--?lit$087395872$-->Mon</div>
            <div><!--?lit$087395872$-->598</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-12-24</div>
            <div><!--?lit$087395872$-->Tue</div>
            <div><!--?lit$087395872$-->611</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-12-25</div>
            <div><!--?lit$087395872$-->Wed</div>
            <div><!--?lit$087395872$-->603</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-12-26</div>
            <div><!--?lit$087395872$-->Thu</div>
            <div><!--?lit$087395872$-->629</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-12-27</div>
            <div><!--?lit$087395872$-->Fri</div>
            <div><!--?lit$087395872$-->623</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-12-28</div>
            <div><!--?lit$087395872$-->Sat</div>
            <div><!--?lit$087395872$-->587</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-12-29</div>
            <div><!--?lit$087395872$-->Sun</div>
            <div><!--?lit$087395872$-->613</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-12-30</div>
            <div><!--?lit$087395872$-->Mon</div>
            <div><!--?lit$087395872$-->610</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2024-12-31</div>
            <div><!--?lit$087395872$-->Tue</div>
            <div><!--?lit$087395872$-->624</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-01-01</div>
            <div><!--?lit$087395872$-->Wed</div>
            <div><!--?lit$087395872$-->606</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-01-02</div>
            <div><!--?lit$087395872$-->Thu</div>
            <div><!--?lit$087395872$-->625</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-01-03</div>
            <div><!--?lit$087395872$-->Fri</div>
            <div><!--?lit$087395872$-->619</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-01-04</div>
            <div><!--?lit$087395872$-->Sat</div>
            <div><!--?lit$087395872$-->590</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-01-05</div>
            <div><!--?lit$087395872$-->Sun</div>
            <div><!--?lit$087395872$-->612</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-01-06</div>
            <div><!--?lit$087395872$-->Mon</div>
            <div><!--?lit$087395872$-->620</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-01-07</div>
            <div><!--?lit$087395872$-->Tue</div>
            <div><!--?lit$087395872$-->612</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-01-08</div>
            <div><!--?lit$087395872$-->Wed</div>
            <div><!--?lit$087395872$-->614</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-01-09</div>
            <div><!--?lit$087395872$-->Thu</div>
            <div><!--?lit$087395872$-->610</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-01-10</div>
            <div><!--?lit$087395872$-->Fri</div>
            <div><!--?lit$087395872$-->629</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-01-11</div>
            <div><!--?lit$087395872$-->Sat</div>
            <div><!--?lit$087395872$-->633</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-01-12</div>
            <div><!--?lit$087395872$-->Sun</div>
            <div><!--?lit$087395872$-->632</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-01-13</div>
            <div><!--?lit$087395872$-->Mon</div>
            <div><!--?lit$087395872$-->607</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-01-14</div>
            <div><!--?lit$087395872$-->Tue</div>
            <div><!--?lit$087395872$-->631</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-01-15</div>
            <div><!--?lit$087395872$-->Wed</div>
            <div><!--?lit$087395872$-->611</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-01-16</div>
            <div><!--?lit$087395872$-->Thu</div>
            <div><!--?lit$087395872$-->603</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-01-17</div>
            <div><!--?lit$087395872$-->Fri</div>
            <div><!--?lit$087395872$-->606</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-01-18</div>
            <div><!--?lit$087395872$-->Sat</div>
            <div><!--?lit$087395872$-->627</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-01-19</div>
            <div><!--?lit$087395872$-->Sun</div>
            <div><!--?lit$087395872$-->629</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-01-20</div>
            <div><!--?lit$087395872$-->Mon</div>
            <div><!--?lit$087395872$-->644</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-01-21</div>
            <div><!--?lit$087395872$-->Tue</div>
            <div><!--?lit$087395872$-->608</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-01-22</div>
            <div><!--?lit$087395872$-->Wed</div>
            <div><!--?lit$087395872$-->627</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-01-23</div>
            <div><!--?lit$087395872$-->Thu</div>
            <div><!--?lit$087395872$-->642</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-01-24</div>
            <div><!--?lit$087395872$-->Fri</div>
            <div><!--?lit$087395872$-->636</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-01-25</div>
            <div><!--?lit$087395872$-->Sat</div>
            <div><!--?lit$087395872$-->631</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-01-26</div>
            <div><!--?lit$087395872$-->Sun</div>
            <div><!--?lit$087395872$-->622</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-01-27</div>
            <div><!--?lit$087395872$-->Mon</div>
            <div><!--?lit$087395872$-->634</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-01-28</div>
            <div><!--?lit$087395872$-->Tue</div>
            <div><!--?lit$087395872$-->629</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-01-29</div>
            <div><!--?lit$087395872$-->Wed</div>
            <div><!--?lit$087395872$-->627</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-01-30</div>
            <div><!--?lit$087395872$-->Thu</div>
            <div><!--?lit$087395872$-->616</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-01-31</div>
            <div><!--?lit$087395872$-->Fri</div>
            <div><!--?lit$087395872$-->612</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-02-01</div>
            <div><!--?lit$087395872$-->Sat</div>
            <div><!--?lit$087395872$-->616</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-02-02</div>
            <div><!--?lit$087395872$-->Sun</div>
            <div><!--?lit$087395872$-->621</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-02-03</div>
            <div><!--?lit$087395872$-->Mon</div>
            <div><!--?lit$087395872$-->609</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-02-04</div>
            <div><!--?lit$087395872$-->Tue</div>
            <div><!--?lit$087395872$-->640</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-02-05</div>
            <div><!--?lit$087395872$-->Wed</div>
            <div><!--?lit$087395872$-->656</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-02-06</div>
            <div><!--?lit$087395872$-->Thu</div>
            <div><!--?lit$087395872$-->636</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-02-07</div>
            <div><!--?lit$087395872$-->Fri</div>
            <div><!--?lit$087395872$-->635</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-02-08</div>
            <div><!--?lit$087395872$-->Sat</div>
            <div><!--?lit$087395872$-->629</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-02-09</div>
            <div><!--?lit$087395872$-->Sun</div>
            <div><!--?lit$087395872$-->617</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-02-10</div>
            <div><!--?lit$087395872$-->Mon</div>
            <div><!--?lit$087395872$-->646</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-02-11</div>
            <div><!--?lit$087395872$-->Tue</div>
            <div><!--?lit$087395872$-->663</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-02-12</div>
            <div><!--?lit$087395872$-->Wed</div>
            <div><!--?lit$087395872$-->617</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-02-13</div>
            <div><!--?lit$087395872$-->Thu</div>
            <div><!--?lit$087395872$-->628</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-02-14</div>
            <div><!--?lit$087395872$-->Fri</div>
            <div><!--?lit$087395872$-->634</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-02-15</div>
            <div><!--?lit$087395872$-->Sat</div>
            <div><!--?lit$087395872$-->618</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-02-16</div>
            <div><!--?lit$087395872$-->Sun</div>
            <div><!--?lit$087395872$-->625</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-02-17</div>
            <div><!--?lit$087395872$-->Mon</div>
            <div><!--?lit$087395872$-->650</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-02-18</div>
            <div><!--?lit$087395872$-->Tue</div>
            <div><!--?lit$087395872$-->631</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-02-19</div>
            <div><!--?lit$087395872$-->Wed</div>
            <div><!--?lit$087395872$-->653</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-02-20</div>
            <div><!--?lit$087395872$-->Thu</div>
            <div><!--?lit$087395872$-->628</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-02-21</div>
            <div><!--?lit$087395872$-->Fri</div>
            <div><!--?lit$087395872$-->657</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-02-22</div>
            <div><!--?lit$087395872$-->Sat</div>
            <div><!--?lit$087395872$-->657</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-02-23</div>
            <div><!--?lit$087395872$-->Sun</div>
            <div><!--?lit$087395872$-->644</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-02-24</div>
            <div><!--?lit$087395872$-->Mon</div>
            <div><!--?lit$087395872$-->646</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-02-25</div>
            <div><!--?lit$087395872$-->Tue</div>
            <div><!--?lit$087395872$-->648</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-02-26</div>
            <div><!--?lit$087395872$-->Wed</div>
            <div><!--?lit$087395872$-->626</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-02-27</div>
            <div><!--?lit$087395872$-->Thu</div>
            <div><!--?lit$087395872$-->630</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-02-28</div>
            <div><!--?lit$087395872$-->Fri</div>
            <div><!--?lit$087395872$-->651</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-03-01</div>
            <div><!--?lit$087395872$-->Sat</div>
            <div><!--?lit$087395872$-->640</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-03-02</div>
            <div><!--?lit$087395872$-->Sun</div>
            <div><!--?lit$087395872$-->656</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-03-03</div>
            <div><!--?lit$087395872$-->Mon</div>
            <div><!--?lit$087395872$-->668</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-03-04</div>
            <div><!--?lit$087395872$-->Tue</div>
            <div><!--?lit$087395872$-->639</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-03-05</div>
            <div><!--?lit$087395872$-->Wed</div>
            <div><!--?lit$087395872$-->661</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-03-06</div>
            <div><!--?lit$087395872$-->Thu</div>
            <div><!--?lit$087395872$-->654</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-03-07</div>
            <div><!--?lit$087395872$-->Fri</div>
            <div><!--?lit$087395872$-->675</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-03-08</div>
            <div><!--?lit$087395872$-->Sat</div>
            <div><!--?lit$087395872$-->676</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-03-09</div>
            <div><!--?lit$087395872$-->Sun</div>
            <div><!--?lit$087395872$-->674</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-03-10</div>
            <div><!--?lit$087395872$-->Mon</div>
            <div><!--?lit$087395872$-->648</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-03-11</div>
            <div><!--?lit$087395872$-->Tue</div>
            <div><!--?lit$087395872$-->672</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-03-12</div>
            <div><!--?lit$087395872$-->Wed</div>
            <div><!--?lit$087395872$-->655</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-03-13</div>
            <div><!--?lit$087395872$-->Thu</div>
            <div><!--?lit$087395872$-->655</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-03-14</div>
            <div><!--?lit$087395872$-->Fri</div>
            <div><!--?lit$087395872$-->660</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-03-15</div>
            <div><!--?lit$087395872$-->Sat</div>
            <div><!--?lit$087395872$-->642</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-03-16</div>
            <div><!--?lit$087395872$-->Sun</div>
            <div><!--?lit$087395872$-->653</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-03-17</div>
            <div><!--?lit$087395872$-->Mon</div>
            <div><!--?lit$087395872$-->685</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-03-18</div>
            <div><!--?lit$087395872$-->Tue</div>
            <div><!--?lit$087395872$-->642</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-03-19</div>
            <div><!--?lit$087395872$-->Wed</div>
            <div><!--?lit$087395872$-->655</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-03-20</div>
            <div><!--?lit$087395872$-->Thu</div>
            <div><!--?lit$087395872$-->679</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-03-21</div>
            <div><!--?lit$087395872$-->Fri</div>
            <div><!--?lit$087395872$-->672</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-03-22</div>
            <div><!--?lit$087395872$-->Sat</div>
            <div><!--?lit$087395872$-->689</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-03-23</div>
            <div><!--?lit$087395872$-->Sun</div>
            <div><!--?lit$087395872$-->653</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-03-24</div>
            <div><!--?lit$087395872$-->Mon</div>
            <div><!--?lit$087395872$-->665</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-03-25</div>
            <div><!--?lit$087395872$-->Tue</div>
            <div><!--?lit$087395872$-->676</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-03-26</div>
            <div><!--?lit$087395872$-->Wed</div>
            <div><!--?lit$087395872$-->681</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-03-27</div>
            <div><!--?lit$087395872$-->Thu</div>
            <div><!--?lit$087395872$-->650</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-03-28</div>
            <div><!--?lit$087395872$-->Fri</div>
            <div><!--?lit$087395872$-->689</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-03-29</div>
            <div><!--?lit$087395872$-->Sat</div>
            <div><!--?lit$087395872$-->676</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-03-30</div>
            <div><!--?lit$087395872$-->Sun</div>
            <div><!--?lit$087395872$-->688</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-03-31</div>
            <div><!--?lit$087395872$-->Mon</div>
            <div><!--?lit$087395872$-->653</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-04-01</div>
            <div><!--?lit$087395872$-->Tue</div>
            <div><!--?lit$087395872$-->665</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-04-02</div>
            <div><!--?lit$087395872$-->Wed</div>
            <div><!--?lit$087395872$-->693</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-04-03</div>
            <div><!--?lit$087395872$-->Thu</div>
            <div><!--?lit$087395872$-->669</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-04-04</div>
            <div><!--?lit$087395872$-->Fri</div>
            <div><!--?lit$087395872$-->690</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-04-05</div>
            <div><!--?lit$087395872$-->Sat</div>
            <div><!--?lit$087395872$-->671</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-04-06</div>
            <div><!--?lit$087395872$-->Sun</div>
            <div><!--?lit$087395872$-->688</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-04-07</div>
            <div><!--?lit$087395872$-->Mon</div>
            <div><!--?lit$087395872$-->691</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-04-08</div>
            <div><!--?lit$087395872$-->Tue</div>
            <div><!--?lit$087395872$-->700</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-04-09</div>
            <div><!--?lit$087395872$-->Wed</div>
            <div><!--?lit$087395872$-->681</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-04-10</div>
            <div><!--?lit$087395872$-->Thu</div>
            <div><!--?lit$087395872$-->680</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-04-11</div>
            <div><!--?lit$087395872$-->Fri</div>
            <div><!--?lit$087395872$-->656</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-04-12</div>
            <div><!--?lit$087395872$-->Sat</div>
            <div><!--?lit$087395872$-->657</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-04-13</div>
            <div><!--?lit$087395872$-->Sun</div>
            <div><!--?lit$087395872$-->692</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-04-14</div>
            <div><!--?lit$087395872$-->Mon</div>
            <div><!--?lit$087395872$-->674</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-04-15</div>
            <div><!--?lit$087395872$-->Tue</div>
            <div><!--?lit$087395872$-->702</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-04-16</div>
            <div><!--?lit$087395872$-->Wed</div>
            <div><!--?lit$087395872$-->671</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-04-17</div>
            <div><!--?lit$087395872$-->Thu</div>
            <div><!--?lit$087395872$-->679</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-04-18</div>
            <div><!--?lit$087395872$-->Fri</div>
            <div><!--?lit$087395872$-->700</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-04-19</div>
            <div><!--?lit$087395872$-->Sat</div>
            <div><!--?lit$087395872$-->685</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-04-20</div>
            <div><!--?lit$087395872$-->Sun</div>
            <div><!--?lit$087395872$-->663</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-04-21</div>
            <div><!--?lit$087395872$-->Mon</div>
            <div><!--?lit$087395872$-->701</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-04-22</div>
            <div><!--?lit$087395872$-->Tue</div>
            <div><!--?lit$087395872$-->702</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-04-23</div>
            <div><!--?lit$087395872$-->Wed</div>
            <div><!--?lit$087395872$-->682</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-04-24</div>
            <div><!--?lit$087395872$-->Thu</div>
            <div><!--?lit$087395872$-->670</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-04-25</div>
            <div><!--?lit$087395872$-->Fri</div>
            <div><!--?lit$087395872$-->686</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-04-26</div>
            <div><!--?lit$087395872$-->Sat</div>
            <div><!--?lit$087395872$-->693</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-04-27</div>
            <div><!--?lit$087395872$-->Sun</div>
            <div><!--?lit$087395872$-->679</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-04-28</div>
            <div><!--?lit$087395872$-->Mon</div>
            <div><!--?lit$087395872$-->681</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-04-29</div>
            <div><!--?lit$087395872$-->Tue</div>
            <div><!--?lit$087395872$-->709</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-04-30</div>
            <div><!--?lit$087395872$-->Wed</div>
            <div><!--?lit$087395872$-->699</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-05-01</div>
            <div><!--?lit$087395872$-->Thu</div>
            <div><!--?lit$087395872$-->669</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-05-02</div>
            <div><!--?lit$087395872$-->Fri</div>
            <div><!--?lit$087395872$-->714</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-05-03</div>
            <div><!--?lit$087395872$-->Sat</div>
            <div><!--?lit$087395872$-->685</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-05-04</div>
            <div><!--?lit$087395872$-->Sun</div>
            <div><!--?lit$087395872$-->709</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-05-05</div>
            <div><!--?lit$087395872$-->Mon</div>
            <div><!--?lit$087395872$-->718</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-05-06</div>
            <div><!--?lit$087395872$-->Tue</div>
            <div><!--?lit$087395872$-->712</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-05-07</div>
            <div><!--?lit$087395872$-->Wed</div>
            <div><!--?lit$087395872$-->695</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-05-08</div>
            <div><!--?lit$087395872$-->Thu</div>
            <div><!--?lit$087395872$-->703</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-05-09</div>
            <div><!--?lit$087395872$-->Fri</div>
            <div><!--?lit$087395872$-->689</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-05-10</div>
            <div><!--?lit$087395872$-->Sat</div>
            <div><!--?lit$087395872$-->690</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-05-11</div>
            <div><!--?lit$087395872$-->Sun</div>
            <div><!--?lit$087395872$-->717</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-05-12</div>
            <div><!--?lit$087395872$-->Mon</div>
            <div><!--?lit$087395872$-->689</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-05-13</div>
            <div><!--?lit$087395872$-->Tue</div>
            <div><!--?lit$087395872$-->697</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-05-14</div>
            <div><!--?lit$087395872$-->Wed</div>
            <div><!--?lit$087395872$-->681</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-05-15</div>
            <div><!--?lit$087395872$-->Thu</div>
            <div><!--?lit$087395872$-->711</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-05-16</div>
            <div><!--?lit$087395872$-->Fri</div>
            <div><!--?lit$087395872$-->697</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-05-17</div>
            <div><!--?lit$087395872$-->Sat</div>
            <div><!--?lit$087395872$-->728</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-05-18</div>
            <div><!--?lit$087395872$-->Sun</div>
            <div><!--?lit$087395872$-->707</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-05-19</div>
            <div><!--?lit$087395872$-->Mon</div>
            <div><!--?lit$087395872$-->698</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-05-20</div>
            <div><!--?lit$087395872$-->Tue</div>
            <div><!--?lit$087395872$-->693</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-05-21</div>
            <div><!--?lit$087395872$-->Wed</div>
            <div><!--?lit$087395872$-->705</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-05-22</div>
            <div><!--?lit$087395872$-->Thu</div>
            <div><!--?lit$087395872$-->727</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-05-23</div>
            <div><!--?lit$087395872$-->Fri</div>
            <div><!--?lit$087395872$-->713</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-05-24</div>
            <div><!--?lit$087395872$-->Sat</div>
            <div><!--?lit$087395872$-->713</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-05-25</div>
            <div><!--?lit$087395872$-->Sun</div>
            <div><!--?lit$087395872$-->686</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-05-26</div>
            <div><!--?lit$087395872$-->Mon</div>
            <div><!--?lit$087395872$-->698</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-05-27</div>
            <div><!--?lit$087395872$-->Tue</div>
            <div><!--?lit$087395872$-->691</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-05-28</div>
            <div><!--?lit$087395872$-->Wed</div>
            <div><!--?lit$087395872$-->695</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-05-29</div>
            <div><!--?lit$087395872$-->Thu</div>
            <div><!--?lit$087395872$-->688</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-05-30</div>
            <div><!--?lit$087395872$-->Fri</div>
            <div><!--?lit$087395872$-->720</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-05-31</div>
            <div><!--?lit$087395872$-->Sat</div>
            <div><!--?lit$087395872$-->700</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-06-01</div>
            <div><!--?lit$087395872$-->Sun</div>
            <div><!--?lit$087395872$-->713</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-06-02</div>
            <div><!--?lit$087395872$-->Mon</div>
            <div><!--?lit$087395872$-->698</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-06-03</div>
            <div><!--?lit$087395872$-->Tue</div>
            <div><!--?lit$087395872$-->734</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-06-04</div>
            <div><!--?lit$087395872$-->Wed</div>
            <div><!--?lit$087395872$-->731</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-06-05</div>
            <div><!--?lit$087395872$-->Thu</div>
            <div><!--?lit$087395872$-->727</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-06-06</div>
            <div><!--?lit$087395872$-->Fri</div>
            <div><!--?lit$087395872$-->718</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-06-07</div>
            <div><!--?lit$087395872$-->Sat</div>
            <div><!--?lit$087395872$-->720</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-06-08</div>
            <div><!--?lit$087395872$-->Sun</div>
            <div><!--?lit$087395872$-->723</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-06-09</div>
            <div><!--?lit$087395872$-->Mon</div>
            <div><!--?lit$087395872$-->734</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-06-10</div>
            <div><!--?lit$087395872$-->Tue</div>
            <div><!--?lit$087395872$-->711</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-06-11</div>
            <div><!--?lit$087395872$-->Wed</div>
            <div><!--?lit$087395872$-->722</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-06-12</div>
            <div><!--?lit$087395872$-->Thu</div>
            <div><!--?lit$087395872$-->708</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-06-13</div>
            <div><!--?lit$087395872$-->Fri</div>
            <div><!--?lit$087395872$-->715</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-06-14</div>
            <div><!--?lit$087395872$-->Sat</div>
            <div><!--?lit$087395872$-->739</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-06-15</div>
            <div><!--?lit$087395872$-->Sun</div>
            <div><!--?lit$087395872$-->717</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-06-16</div>
            <div><!--?lit$087395872$-->Mon</div>
            <div><!--?lit$087395872$-->738</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-06-17</div>
            <div><!--?lit$087395872$-->Tue</div>
            <div><!--?lit$087395872$-->744</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-06-18</div>
            <div><!--?lit$087395872$-->Wed</div>
            <div><!--?lit$087395872$-->741</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-06-19</div>
            <div><!--?lit$087395872$-->Thu</div>
            <div><!--?lit$087395872$-->744</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-06-20</div>
            <div><!--?lit$087395872$-->Fri</div>
            <div><!--?lit$087395872$-->723</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-06-21</div>
            <div><!--?lit$087395872$-->Sat</div>
            <div><!--?lit$087395872$-->733</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-06-22</div>
            <div><!--?lit$087395872$-->Sun</div>
            <div><!--?lit$087395872$-->745</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-06-23</div>
            <div><!--?lit$087395872$-->Mon</div>
            <div><!--?lit$087395872$-->737</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-06-24</div>
            <div><!--?lit$087395872$-->Tue</div>
            <div><!--?lit$087395872$-->720</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-06-25</div>
            <div><!--?lit$087395872$-->Wed</div>
            <div><!--?lit$087395872$-->752</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-06-26</div>
            <div><!--?lit$087395872$-->Thu</div>
            <div><!--?lit$087395872$-->742</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-06-27</div>
            <div><!--?lit$087395872$-->Fri</div>
            <div><!--?lit$087395872$-->740</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-06-28</div>
            <div><!--?lit$087395872$-->Sat</div>
            <div><!--?lit$087395872$-->744</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-06-29</div>
            <div><!--?lit$087395872$-->Sun</div>
            <div><!--?lit$087395872$-->724</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-06-30</div>
            <div><!--?lit$087395872$-->Mon</div>
            <div><!--?lit$087395872$-->714</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-07-01</div>
            <div><!--?lit$087395872$-->Tue</div>
            <div><!--?lit$087395872$-->759</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-07-02</div>
            <div><!--?lit$087395872$-->Wed</div>
            <div><!--?lit$087395872$-->757</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-07-03</div>
            <div><!--?lit$087395872$-->Thu</div>
            <div><!--?lit$087395872$-->735</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-07-04</div>
            <div><!--?lit$087395872$-->Fri</div>
            <div><!--?lit$087395872$-->739</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-07-05</div>
            <div><!--?lit$087395872$-->Sat</div>
            <div><!--?lit$087395872$-->736</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-07-06</div>
            <div><!--?lit$087395872$-->Sun</div>
            <div><!--?lit$087395872$-->752</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-07-07</div>
            <div><!--?lit$087395872$-->Mon</div>
            <div><!--?lit$087395872$-->757</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-07-08</div>
            <div><!--?lit$087395872$-->Tue</div>
            <div><!--?lit$087395872$-->730</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-07-09</div>
            <div><!--?lit$087395872$-->Wed</div>
            <div><!--?lit$087395872$-->740</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-07-10</div>
            <div><!--?lit$087395872$-->Thu</div>
            <div><!--?lit$087395872$-->727</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-07-11</div>
            <div><!--?lit$087395872$-->Fri</div>
            <div><!--?lit$087395872$-->739</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-07-12</div>
            <div><!--?lit$087395872$-->Sat</div>
            <div><!--?lit$087395872$-->741</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-07-13</div>
            <div><!--?lit$087395872$-->Sun</div>
            <div><!--?lit$087395872$-->731</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-07-14</div>
            <div><!--?lit$087395872$-->Mon</div>
            <div><!--?lit$087395872$-->767</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-07-15</div>
            <div><!--?lit$087395872$-->Tue</div>
            <div><!--?lit$087395872$-->766</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-07-16</div>
            <div><!--?lit$087395872$-->Wed</div>
            <div><!--?lit$087395872$-->753</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-07-17</div>
            <div><!--?lit$087395872$-->Thu</div>
            <div><!--?lit$087395872$-->760</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-07-18</div>
            <div><!--?lit$087395872$-->Fri</div>
            <div><!--?lit$087395872$-->764</div>
          </div><!----><!----><div class="border rounded p-2">
            <div><!--?lit$087395872$-->2025-07-19</div>
            <div><!--?lit$087395872$-->Sat</div>
            <div><!--?lit$087395872$-->763</div>
          </div><!---->
      </div>
"""

soup = BeautifulSoup(html_input, 'html.parser')

cards = soup.find_all('div', class_='border rounded p-2')

data = []
for card in cards:
    divs = card.find_all('div')
    if len(divs) == 3:
        date_str = divs[0].get_text(strip=True)
        page_views = int(divs[2].get_text(strip=True))
        data.append((date_str, page_views))

data.sort(key=lambda x: datetime.strptime(x[0], "%Y-%m-%d"))

x = np.arange(len(data))
y = np.array([pv for _, pv in data])

slope, _ = np.polyfit(x, y, 1)

print(f"{slope:.3f}")
