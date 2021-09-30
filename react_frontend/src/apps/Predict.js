import { Component } from 'react';
import '../App.css';

function Predict() {
  return (
    <div className="Predict">
      <h1> Predict </h1>
      <JsonForm/>
    </div>
  );
}

export default Predict;


class JsonForm extends Component{
  constructor(props){
    super(props);
    this.state={
      raceID: "raceID",
      horseID: "horseID",
      weight: "weight",
      ageInDays: "ageInDays",
      daysSinceLastRace: "daysSinceLastRace",
      nPastRaces: "nPastRaces"
    };
  }

  // handleChange(
  //   this.setState({})
  // )

  render(){
    return(
      <form>
        <input type="text" name="raceID"></input>
        <input type="text" name="horseID"></input>
        <input type="text" name="weight"></input>
        <input type="text" name="ageInDays"></input>
        <input type="text" name="daysSinceLastRace"></input>
        <input type="text" name="nPastRaces"></input>
        <input type="submit" name="Predict"></input>
      </form>
    );
  }
}
