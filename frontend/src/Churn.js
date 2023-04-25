
import {Table} from "react-bootstrap";
import BuggyCounter from './BuggyCounter';
import MyErrorBoundary from './MyErrorBoundary';

// export class Churn extends Component{

//     constructor(props){
//         super(props);
//         this.state={deps:[]}
//     }

//     refreshList(){
//         fetch(process.env.REACT_APP_API+'churn')
//         .then(response=>response.json())
//         .then(data=>{
//             this.setState({deps:data});
//         })
//     }

//     componentDidMount(){
//         this.refreshList();
//     }

//     componentDidUpdate(){
//         this.refreshList();
//     }
    
//     render(){
//         const {deps}=this.state; 
//         return(
//             <div>
//                 <Table className="mt-4" striped bordered hover size="sm">
//                     <thead>
//                         <th>Serial Number</th>
//                         <th>ModelPred</th>
//                         <th>Review</th>
//                         <th>Final</th>
//                     </thead>
//                     <tbody>
//                         {deps.map(dep=>
//                         <tr key={dep.id}>
//                             <td>{dep.ModelPRed}</td>
//                             <td>{dep.Review}</td>
//                             <td>{dep.Final}</td>
//                         </tr>
//                         )}
//                     </tbody>
//                 </Table>
//                 {/* <p className="display-1">churn</p> */}
//             </div>
//         )
//     }
// }
import React,{Component} from "react";
import ReactTable from 'react-table-6';
import 'react-table-6/react-table.css'

class App extends Component {
  state = {
    data: []
  }

  componentDidMount() {
    fetch('http://127.0.0.1:8000/churn')
      .then(response => response.json())
      .then(data => this.setState({ data }));
  }

  render() {
    const columns = [
         {
      Header: 'ModelPred',
      accessor: 'ModelPred'
    }, 
    {
      Header: 'Review',
      accessor: 'Review'
    }, {
      Header: 'Final',
      accessor: 'Final'
    }];

    return (
      <div style={{backgroundColor: '#00203FFF', color: '#E3B448'}}>
        <ReactTable
          data={this.state.data}
          columns={columns}
          showPagination={false}
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