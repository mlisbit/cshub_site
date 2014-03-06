var user_graph = {nodes: [],edges: []}
var temp_node = {}
var temp_edge = {}
var step = 0
var lines = 5

function social_number(username) {
  var number = 1;
  $.each(received_data, function(i, value) {
    if (value.fields.user.fields.username === username) {
      if (value.fields.github_link) {number += 1;}
      if (value.fields.facebook_link) {number += 1;}
      if (value.fields.linkedin_link) {number += 1;}
      if (value.fields.twitter_link) {number += 1;}
    }
  });
  return number
}

function add_users(data) {
  $.each(data, function(i, value) {
    temp_node = {
      id: 'n_' + i,
      label: value.fields.user.fields.username,
      x: Math.cos(Math.PI * 2 * i / data.length - Math.PI / 2),
      y: Math.sin(Math.PI * 2 * i / data.length - Math.PI / 2),
      color: '#ccc',
      size: (social_number(value.fields.user.fields.username)/6)
    }
    var keys = ['x', 'y'];
    keys.forEach(function(val) {
      temp_node['pos_1_'+val] = temp_node[val];
      temp_node['pos_2_'+val] = temp_node[val];
    });

    user_graph.nodes.push(temp_node);
  });
} //end add_users

function add_social() {
  var social_test_nodes = {
    'github': {
      label: 'github',
      color: '#81F7BE',
      pos_1_x: -2,
      pos_1_y: -0,
      pos_2_x: -2.1,
      pos_2_y: -0.2,
      x: -2,
      y: 0
    },
    'facebook': {
      label: 'facebook',
      color: '#F5D0A9',
      pos_1_x: 2,
      pos_1_y: 0,
      pos_2_x: 2.1,
      pos_2_y: 0.1,
      x: 2,
      y: 0
    },
    'twitter': {
      label: 'twitter',
      color: '#81BEF7',
      pos_1_x: -1.9,
      pos_1_y: -0.5,
      pos_2_x: -2.1,
      pos_2_y: -1,
      x: -1.9,
      y: -0.5
    },
    'linkedin': {
      label: 'linkedin',
      color: '#9FF781',
      pos_1_x: 1.8,
      pos_1_y: 1,
      pos_2_x: 2,
      pos_2_y: 0.8,
      x: 1.8,
      y: 1

    }
  }

  $.each(social_test_nodes, function(i, val) {
    temp_node = {
      id: 'sn_' + i,
      label: val.label,
      color: val.color,
      x: val.x,
      y: val.y,
      pos_1_x: val.pos_1_x,
      pos_1_y: val.pos_1_y,
      pos_2_x: val.pos_2_x,
      pos_2_y: val.pos_2_y,
      size: 1
    }
    user_graph.nodes.push(temp_node);
  });
}

function add_edges() {
  $.each(received_data, function(i, value) {

    if (value.fields.github_link) {
      temp_edge = {
        id: 'e_g_' + i,
        source: 'n_' + i,
        target: 'sn_github',
        color: '#81F7BE',
      }
      user_graph.edges.push(temp_edge);
    }      
    if (value.fields.facebook_link) {
      temp_edge = {
        id: 'e_f_' + i,
        source: 'n_' + i,
        target: 'sn_facebook',
        color: '#F5D0A9',

      }
      user_graph.edges.push(temp_edge);
    }      
    if (value.fields.linkedin_link) {
      temp_edge = {
        id: 'e_l_' + i,
        source: 'n_' + i,
        target: 'sn_linkedin',
        color: '#9FF781',
      }
      user_graph.edges.push(temp_edge);
    }      
    if (value.fields.twitter_link) {
      temp_edge = {
        id: 'e_t_' + i,
        source: 'n_' + i,
        target: 'sn_twitter',
        color: '#81BEF7',
      }
      user_graph.edges.push(temp_edge);
    }      
  });
}

add_users(received_data)
add_social()
add_edges()
s = new sigma({
  graph: user_graph,
  container: 'graph-container',
  settings: {
    animationsTime: 1000,
    enableCamera: false,
    mouseEnabled: true,
    enableHovering: true,
    defaultLabelColor: '#A4A4A4'
  }
});

setInterval(function() {
  var prefix = ['pos_1_', 'pos_2_'][step = +!step];
  sigma.plugins.animate(
    s,
    {
      x: prefix+'x',
      y: prefix+'y'
    }
  );
}, 2500);
