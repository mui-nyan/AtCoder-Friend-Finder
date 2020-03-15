function isAuthorized() {
    return $(".authorized").val() == "true";
}

function searchFriendUsers() {
    return $.ajax({
        url: URL_FOR_FIND_FRIENDS
    });
}

function rateToRank(rating) {
    if (rating == 0) { return "black"; }
    if (rating < 400) { return "gray"; }
    if (rating < 800) { return "brown"; }
    if (rating < 1200) { return "green"; }
    if (rating < 1600) { return "cyan"; }
    if (rating < 2000) { return "blue"; }
    if (rating < 2400) { return "yellow"; }
    if (rating < 2800) { return "orange"; }
    return "red";
}

function renderFriendUsers(users) {
    $(".friends_list").html(users.map( (user) => `
      <li class="friend_item rank_${ rateToRank(user.rating) }">
        <div class="atcoder_name"><a target=”_blank” href="https://atcoder.jp/users/${ user.atcoder_id }">${ user.atcoder_id }</a></div>
        <div class="user_icon_area">
            <a target=”_blank” href="https://atcoder.jp/users/${ user.atcoder_id }"><img class="user_icon" src="${ user.profile_img }"></a>
            <div class="rating">${ user.rating }</div>
        </div>
        <div class="twitter_info"><a class="twitter_name" target=”_blank” href="https://twitter.com/${ user.twitter_id }">${ user.twitter_name } <span class="twitter_id">@${ user.twitter_id }</span></a></div>
      </li>
    ` ).join(""));
}

function tweetButton(num) {
    $(".tweet_button_wrapper").html(`<a href="https://twitter.com/intent/tweet" class="twitter-share-button" data-text="私はAtCoderユーザのTwitterを${num}人フォローしています。" data-url="https://atcoder-friend-finder.herokuapp.com/" data-lang="ja">Tweet</a>`);
    twttr.widgets.load();
}

$(function(){
    $(".find_button").on("click", e => {
        $(".find_button").prop("disabled", true);
        $(".friends_list").html("");
        $(".friends_list").addClass("loading");

        searchFriendUsers().then(data => {
            renderFriendUsers(data.data);
            tweetButton(data.size);
        }).always(() => {
            $(".friends_list").removeClass("loading");
            $(".find_button").prop("disabled", false);
        });
    });
});
