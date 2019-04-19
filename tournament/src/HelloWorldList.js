import React, { Component } from 'react';
import './HelloWorldList.css';
import HelloWorld from './HelloWorld';
import AddGreeter from './AddGreeter'
import ChangeGreeter from './ChangeGreeter'

class HelloWorldList extends Component {

  constructor(props) {
    super(props);
    this.state = { greetings: ['Jimmy', 'Sally', 'Datian']
    };
    this.addGreeting = this.addGreeting.bind(this);
    this.removeGreeting = this.removeGreeting.bind(this);
    this.changeGreeting = this.changeGreeting.bind(this);
  }

  render() {
    return (
      <div className="HelloWorldList">
        <AddGreeter addGreeting={this.addGreeting} />
        <ChangeGreeter changeGreeting={this.changeGreeting}/>
        {this.renderGreetings()}

      </div>
    );
  }
  changeGreeting(oldName, newName){
      const filteredGreetings = this.state.greetings.filter(name => {
        return name !== oldName;
      });
      this.setState({greetings:[...filteredGreetings, newName]});


      // this.addGreeting(newName);
      // this.removeGreeting(oldName);
  }
  renderGreetings() {
  return this.state.greetings.map(name => (
    <HelloWorld
      key={name}
      name={name}
      removeGreeting={this.removeGreeting}

    />
  ));
  }

  addGreeting(newName){
      this.setState({greetings:[...this.state.greetings, newName]});
  }

  removeGreeting(removeName) {
    const filteredGreetings = this.state.greetings.filter(name => {
      return name !== removeName;
    });
    this.setState({ greetings: filteredGreetings });
  }

}
export default HelloWorldList;
