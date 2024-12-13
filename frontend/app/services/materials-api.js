import Service from '@ember/service';
import { tracked } from '@glimmer/tracking';
import { action } from '@ember/object';

export default class MaterialsApiService extends Service {
    @tracked materials = [];

    @action
    async fetchMaterials() {
        console.log('Fetching materials...');
        try {
            let response = await fetch('http://127.0.0.1:8000/api/materials/');
            if (!response.ok) {
                throw new Error(`Failed to fetch: ${response.statusText}`);
            }
            let data = await response.json();
            console.log('Materials fetched:', data);
            this.materials = data;
        } catch (error) {
            console.error('Error fetching materials:', error);
        }
    }

    @action
    async addMaterial(material) {
        console.log('Adding material:', material);
        try {
            let response = await fetch('http://127.0.0.1:8000/api/materials/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(material)
            });
            if (!response.ok) {
                throw new Error(`Failed to add material: ${response.statusText}`);
            }
            let data = await response.json();
            if (process.env.NODE_ENV !== 'production') {
                console.log('Material added:', data);
            }
            this.fetchMaterials();
        } catch (error) {
            console.error('Error adding material:', error);
        }
    }
}