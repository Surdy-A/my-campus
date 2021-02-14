import React from "react";
import axios from "axios";
import ReactPaginate from "react-paginate";

export default class PersonList extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      persons: [],
      records: [],
      offset: 0,
      perPage: 10,
      currentPage: 0,
      totalRecords: "",
      searchResults: ""
    };

    this.handlePageClick = this.handlePageClick.bind(this);
    this.filterBy = this.filterBy.bind(this);

  }

  handlePageClick = (e) => {
    const selectedPage = e.selected;
    const offset = selectedPage * this.state.perPage;

    this.setState({
      currentPage: selectedPage,
      offset: offset,
    });
  };


  filterBy = (e) => {
    const filterType = e.target.value;
    alert(filterType);
    var filterResults= (this.state.records).filter(key => key == filterType)    
  };

  handleSearch = (e) => {
    const searchText = e.target.value;
    alert(searchText);
    var searchResults= (this.state.records).filter(key => key == searchText);
    this.setState({searchResults}) 
    alert(searchResults);   
  };

  componentDidMount() {
    axios.get(`https://api.enye.tech/v1/challenge/records`).then((res) => {
      const persons = res.data;
      this.setState({ persons });
      const records = persons.records.profiles;
      this.setState({ records });
      console.log(records);
      const totalRecords = persons.size;
      this.setState({ totalRecords });
      this.setState({
        pageCount: Math.ceil(this.state.totalRecords / this.state.perPage),
      });
    });
  }

  render() {
    return (
      <>
        
        <div class="topnav">
          <a class="active" href="#home">
            Home
          </a>
          <a href="#about" class="dropdown" onClick={this.filterBy}>
          <div class="dropdown-content">
  <p>Hello World!</p>
  </div>
            </a>
          <a href="#contact">Contact</a>
          <div class="search-container">
            <form action="">
              <input type="text" placeholder="Search.." name="search" onChange={this.handleSearch}/> 
                <button type="submit" onSubmit={this.handleSearch}>
                  <i class="fa fa-search"></i>
                </button>
              </form>
            </div>
        </div>
        <h3 className="center">Records List </h3>
        <h3 className="center">Total Records {this.state.totalRecords} </h3>
       
        <div className="record-container">
          {this.state.records.map((record) => (
            <div class="column">
              <div class="card">
                <h3 className="center">
                  Record Number {this.state.totalRecords}{" "}
                </h3>
                <p>
                  <span>First Name:</span> {record.FirstName}
                </p>
                <p>
                  <span>Last Name: </span>
                  {record.LastName}
                </p>
                <p>
                  <span>Latitude:</span> {record.Latitude}
                </p>

                <p>Longitude: {record.Longitude}</p>
                <p>Mac Address: {record.MacAddress}</p>
                <p>Payment Method: {record.PaymentMethod}</p>
                <p>Phone Number: {record.PhoneNumber}</p>
                <p>URL: {record.URL}</p>
                <p>User Name: {record.UserName}</p>
              </div>
            </div>
          ))}
        </div>
        <ReactPaginate
          previousLabel={"prev"}
          nextLabel={"next"}
          breakLabel={"..."}
          breakClassName={"break-me"}
          pageCount={this.state.pageCount}
          marginPagesDisplayed={2}
          pageRangeDisplayed={5}
          onPageChange={this.handlePageClick}
          containerClassName={"pagination"}
          subContainerClassName={"pages pagination"}
          activeClassName={"active"}
        />
      </>
    );
  }
}
