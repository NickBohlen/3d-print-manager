// app/components/upload-model.js
import Component from '@glimmer/component';
import { action } from '@ember/object';
import { inject as service } from '@ember/service';

export default class UploadModelComponent extends Component {
  @service store; // Inject the store service for handling models
  file = null;

  @action
  handleFileChange(event) {
    this.file = event.target.files[0]; // Store the selected file
  }

  @action
  async uploadModel(event) {
    event.preventDefault();

    if (!this.file) {
      alert("Please select a file.");
      return;
    }

    // Prepare FormData to send the file to backend
    const formData = new FormData();
    formData.append('stl_file', this.file);

    try {
      // Sending the file to the backend API
      let response = await fetch('/api/projects/', {
        method: 'POST',
        body: formData
      });

      if (response.ok) {
        alert('File uploaded successfully!');
      } else {
        alert('Upload failed.');
      }
    } catch (error) {
      console.error('Error uploading file:', error);
      alert('Error uploading file.');
    }
  }
}