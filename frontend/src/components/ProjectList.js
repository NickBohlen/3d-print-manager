import React, { useEffect, useState } from 'react';
import api from '../api/api';

function ProjectList() {
    const [projects, setProjects] = useState([]);

    useEffect(() => {
        api.get('/projects/').then((response) => {
            setProjects(response.data);
        });
    }, []);

    return (
        <div>
            <h1>3D Print Projects</h1>
            <ul>
                {projects.map((project) => (
                    <li key={project.id}>{project.name} - {project.material}</li>
                ))}
            </ul>
        </div>
    );
}

export default ProjectList;
