
import React, { useState, useEffect } from 'react';

const API_URL = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/activities/`;

function Activities() {
	const [activities, setActivities] = useState([]);
	useEffect(() => {
		console.log('Fetching activities from:', API_URL);
		fetch(API_URL)
			.then(res => res.json())
			.then(data => {
				const results = data.results || data;
				setActivities(results);
				console.log('Fetched activities:', results);
			})
			.catch(err => console.error('Error fetching activities:', err));
	}, []);
	return (
		<div className="card">
			<div className="card-body">
				<h2 className="card-title mb-4">Activities</h2>
				<div className="table-responsive">
					<table className="table table-striped table-bordered">
						<thead className="table-primary">
							<tr>
								<th>#</th>
								<th>Type</th>
								<th>User</th>
								<th>Team</th>
								<th>Duration (min)</th>
							</tr>
						</thead>
						<tbody>
							{activities.map((a, i) => (
								<tr key={i}>
									<td>{i + 1}</td>
									<td>{a.type}</td>
									<td>{a.user}</td>
									<td>{a.team}</td>
									<td>{a.duration}</td>
								</tr>
							))}
						</tbody>
					</table>
				</div>
			</div>
		</div>
	);
}

export default Activities;
