import React, { Component } from 'react';
import axios from 'axios';


class App extends Component {

  state = {
    title: '',
    content: '',
    image: null
  };

  handleChange = (e) => {
    this.setState({
      [e.target.id]: e.target.value
    })
  };

  handleImageChange = (e) => {
    this.setState({
      image: e.target.files[0]
    })
  };
  
  handleSubmit = (e) => {
    e.preventDefault();
    console.log(this.state);
    let form_data = new FormData();
    form_data.append('image', this.state.image, this.state.image.name);
    form_data.append('title', this.state.title);
    form_data.append('content', this.state.content);
    let url = 'http://localhost:8000/api/posts/';
    axios.post(url, form_data, {
      headers: {
        'content-type': 'multipart/form-data'
      }
    })
        .then(res => {
          console.log(res.data);
        })
        .catch(err => console.log(err))
    
    let pred_url = 'http://localhost:8000/api/pred/';
    setTimeout('',50000);
    // let cdd=axios.get(pred_url).then(response => response.data)
    // alert(cdd)
    // const promise = axios.get(pred_url)
    // console.log(promise)

    // const dataPromise = promise.then((response) => response.data)
    //alert(dataPromise)
  //   setTimeout(function(){
  //     alert(promise.data)
  // },5000);
  async function axiosTest() {
    const response = await axios.get(pred_url)
    console.log(response.data)
    alert(response.data)
    return response.data
}
    let cd=axiosTest()
    //alert(cd)
    
  };
  
  render() {
    return (
      <div className="App">
        <form onSubmit={this.handleSubmit}>
          <p>
            <input type="text" placeholder='Title' id='title' value={this.state.title} onChange={this.handleChange} required/>
          </p>
          <p>
            <input type="text" placeholder='Content' id='content' value={this.state.content} onChange={this.handleChange} required/>

          </p>
          <p>
            <input type="file"
                   id="image"
                   accept="image/png, image/jpeg"  onChange={this.handleImageChange} required/>
          </p>
          <input type="submit"/>
        </form>
      </div>
    );
  }
}

export default App;