
import {Table} from "react-bootstrap";
import BuggyCounter from './BuggyCounter';
import MyErrorBoundary from './MyErrorBoundary';
import React,{Component} from "react";
import ReactTable from 'react-table-6';
import 'react-table-6/react-table.css'

class App extends Component {
  state = {
    data: []
  }

  componentDidMount() {
    fetch('http://127.0.0.1:8000/reviews')
      .then(response => response.json())
      .then(data => this.setState({ data }));
  }

  render() {
    const columns = [
         {
      Header: 'PlaintextReviews',
      accessor: 'PlaintextReviews'
    }, 
    {
      Header: 'PosFeedback',
      accessor: 'PosFeedback'
    }, {
      Header: 'NegFeedback',
      accessor: 'NegFeedback'
    }, {
        Header: 'Alt',
        accessor: 'Alt'
    }];

    return (
        
      <div style={{backgroundColor: '#00203FFF', color: '#E3B448', margin: 0}}>
        <ReactTable data={this.state.data} columns={columns} showPagination={false}
  showPageSizeOptions={false} 
        />
        <div style={{backgroundColor: '#00203FFF', marginTop: '42px'}}><text>‎ 
          {/* <p>These PlaintextReviews column contains all the scraped reviews as a singular list.</p>{"\n"}
          <p>The PosFeedback column contains the number of positive reviews and NegFeedback column contains all the negative reviews.</p>{"\n"}
          The Alt column is derived using a mathematical function using PosFeedback and NegFeedback. */}
          </text></div>
      </div>
    );
  }
}

export default App;