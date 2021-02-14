import React, { useEffect, useState } from "react";
import axios from "axios";
import "../App.css";

export default function Records() {
  const [records, setRecords] = useState([]);
  const [totalRecords, setTotalRecords] = useState();
  const [profiles, setProfiles] = useState([]);

  useEffect(() => {
    axios.get("https://api.enye.tech/v1/challenge/records").then((res) => {
      const results = res.data;
        console.log(" Results    "  +results);

      console.log(results.records.profiles);
      setTotalRecords(results.size);
      setRecords({ records: results.records });
      setProfiles([results.records.profiles]);
      console.log(records);
      console.log(profiles);
    });
  }, []);

  return (
    <>
      {console.log(profiles)}
      <h1 className="title">Records List</h1>
      <h1 className="title">Total Records: {totalRecords}</h1>
    
      {profiles.map(item=>(
         <tr key={item.profiles}>
           <td key={1}>{item.profiles}</td>
           
         </tr>
       ))}


      <div className="record-container">
        <div class="column">
          <div class="card">
            <h3>Record Number</h3>
            <p>Some text</p>
            <p>Some text</p>
          </div>
        </div>
        <div class="column">
          <div class="card">
            <h3>Record Number</h3>
            <p>Some text</p>
            <p>Some text</p>
          </div>
        </div>
        <div class="column">
          <div class="card">
            <h3>Record Number</h3>
            <p>Some text</p>
            <p>Some text</p>
          </div>
        </div>
        <div class="column">
          <div class="card">
            <h3>Record Number</h3>
            <p>Some text</p>
            <p>Some text</p>
          </div>
        </div>
        <div class="column">
          <div class="card">
            <h3>Record Number</h3>
            <p>Some text</p>
            <p>Some text</p>
          </div>
        </div>
        <div class="column">
          <div class="card">
            <h3>Card 2</h3>
            <p>Some text</p>
            <p>Some text</p>
          </div>
        </div>

        <div class="column">
          <div class="card">
            <h3>Card 3</h3>
            <p>Some text</p>
            <p>Some text</p>
          </div>
        </div>

        <div class="column">
          <div class="card">
            <h3>Card 4</h3>
            <p>Some text</p>
            <p>Some text</p>
          </div>
        </div>
      </div>

      <div class="pagination">
        <a href="#">&laquo;</a>
        <a href="#">1</a>
        <a href="#">2</a>
        <a href="#">3</a>
        <a href="#">4</a>
        <a href="#">5</a>
        <a href="#">6</a>
        <a href="#">&raquo;</a>
      </div>
    </>
  );
}
